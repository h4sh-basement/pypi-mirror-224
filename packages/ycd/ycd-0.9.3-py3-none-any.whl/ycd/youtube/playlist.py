import requests
import re
from . import api
from ..videoinfo2 import VideoInfo


from . import util, yt_data_extract, proto, local_playlist
from . import yt_app
from .. import settings

import base64
import urllib
import json
import string
import gevent
import math
from flask import request
import flask





def playlist_ctoken(playlist_id, offset):

    offset = proto.uint(1, offset)
    # this is just obfuscation as far as I can tell. It doesn't even follow protobuf
    offset = b'PT:' + proto.unpadded_b64encode(offset)
    offset = proto.string(15, offset)

    continuation_info = proto.string( 3, proto.percent_b64encode(offset) )

    playlist_id = proto.string(2, 'VL' + playlist_id )
    pointless_nest = proto.string(80226972, playlist_id + continuation_info)

    return base64.urlsafe_b64encode(pointless_nest).decode('ascii')

# initial request types:
#   polymer_json: https://m.youtube.com/playlist?list=PLv3TTBr1W_9tppikBxAE_G6qjWdBljBHJ&pbj=1&lact=0
#   ajax json:    https://m.youtube.com/playlist?list=PLv3TTBr1W_9tppikBxAE_G6qjWdBljBHJ&pbj=1&lact=0 with header X-YouTube-Client-Version: 1.20180418


# continuation request types:
#   polymer_json: https://m.youtube.com/playlist?&ctoken=[...]&pbj=1
#   ajax json:    https://m.youtube.com/playlist?action_continuation=1&ajax=1&ctoken=[...]


headers_1 = (
    ('Accept', '*/*'),
    ('Accept-Language', 'en-US,en;q=0.5'),
    ('X-YouTube-Client-Name', '2'),
    ('X-YouTube-Client-Version', '2.20180614'),
)

def playlist_first_page(playlist_id, report_text = "Retrieved playlist"):
    url = 'https://m.youtube.com/playlist?list=' + playlist_id + '&pbj=1'
    content = util.fetch_url(url, util.mobile_ua + headers_1, report_text=report_text, debug_name='playlist_first_page')
    content = json.loads(content.decode('utf-8'))

    return content


#https://m.youtube.com/playlist?itct=CBMQybcCIhMIptj9xJaJ2wIV2JKcCh3Idwu-&ctoken=4qmFsgI2EiRWTFBMT3kwajlBdmxWWlB0bzZJa2pLZnB1MFNjeC0tN1BHVEMaDmVnWlFWRHBEUWxFJTNE&pbj=1
def get_videos(playlist_id, page):

    url = "https://m.youtube.com/playlist?ctoken=" + playlist_ctoken(playlist_id, (int(page)-1)*20) + "&pbj=1"
    headers = {
        'User-Agent': '  Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-YouTube-Client-Name': '2',
        'X-YouTube-Client-Version': '2.20180508',
    }

    content = util.fetch_url(url, headers, report_text="Retrieved playlist", debug_name='playlist_videos')

    info = json.loads(content.decode('utf-8'))
    return info


# @yt_app.route('/playlist')
def get_playlist_page(playlist_id, page='1'):
    # if 'list' not in request.args:
    #     abort(400)

    # playlist_id = request.args.get('list')
    # page = request.args.get('page', '1')

    if page == '1':
        first_page_json = playlist_first_page(playlist_id)
        this_page_json = first_page_json
    else:
        tasks = (
            gevent.spawn(playlist_first_page, playlist_id, report_text="Retrieved playlist info" ),
            gevent.spawn(get_videos, playlist_id, page)
        )
        gevent.joinall(tasks)
        util.check_gevent_exceptions(*tasks)
        first_page_json, this_page_json = tasks[0].value, tasks[1].value

    info = yt_data_extract.extract_playlist_info(this_page_json)
    if info['error']:
        return flask.render_template('error.html', error_message = info['error'])

    if page != '1':
        info['metadata'] = yt_data_extract.extract_playlist_metadata(first_page_json)

    util.prefix_urls(info['metadata'])
    for item in info.get('items', ()):
        util.prefix_urls(item)
        util.add_extra_html_info(item)
        if 'id' in item:
            item['thumbnail'] = settings.img_prefix + 'https://i.ytimg.com/vi/' + item['id'] + '/default.jpg'

        item['url'] += '&list=' + playlist_id
        if item['index']:
            item['url'] += '&index=' + str(item['index'])

    video_count = yt_data_extract.deep_get(info, 'metadata', 'video_count')
    if video_count is None:
        video_count = 40

    video_list = info.get('items', [])
    num_pages = math.ceil(video_count/20)
    
    return video_list, num_pages, info['metadata']
    # return flask.render_template('playlist.html',
    #     header_playlist_names = local_playlist.get_playlist_names(),
    #     video_list = info.get('items', []),
    #     num_pages = math.ceil(video_count/20),
    #     parameters_dictionary = request.args,

    #     **info['metadata']
    # ).encode('utf-8')


mobile_user_agent = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
mobile_ua = (('User-Agent', mobile_user_agent),)
headers_mobile = (
    ('Accept', '*/*'),
    ('Accept-Language', 'en-US,en;q=0.5'),
    ('X-YouTube-Client-Name', '2'),
    ('X-YouTube-Client-Version', '2.20180830'),
) + mobile_ua

channel_id_re = re.compile(r'videos\.xml\?channel_id=([a-zA-Z0-9_-]{24})"')
ch_id_pattern_0 = re.compile(r'(^PL[\w-]+)')
ch_id_pattern_1 = re.compile(r'/playlist\?list=(PL[\w-]+)')


def get_playlist_id(base_url):
    match = re.search(ch_id_pattern_0, base_url)
    if match:
        return match.group(1)

    match = re.search(ch_id_pattern_1, base_url)
    if match:
        return match.group(1)
    return None


def get_videos_from_playlist(playlist_id):
    cache = set()
    cache.add("")
    counter = 0
    for items in api.get_video_items(playlist_id):
        for item in items:

            if not item:
                return
            video = parse(item)
            if video.get('id') in cache:
                counter += 1
                if counter > 20:
                    return
                continue
            cache.add(video.get('id'))
            yield video


def parse(item):
    video = dict()
    try:
        video["id"] = item["snippet"]["resourceId"]["videoId"]
        video["title"] = video["time_published"] = item["snippet"]["title"]
        video["time_published"] = item["snippet"]["publishedAt"]
        video["author"] = item["snippet"]["channelTitle"]
        info = VideoInfo(video["id"])
        video['duration'] = info.get_duration()
        return video
    except KeyError as e:
        print(type(e), str(e))
        video["error"] = True
        return video
    except Exception:
        video["error"] = True
        return video


def parse_id(item):
    try:
        video_id = item["snippet"]["resourceId"]["videoId"]
        return video_id
    except KeyError as e:
        print(type(e), str(e))
        return "vid_error"
