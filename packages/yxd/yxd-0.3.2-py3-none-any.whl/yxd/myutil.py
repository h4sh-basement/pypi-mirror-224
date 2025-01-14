import datetime
import requests
import json
import os
import re
from . import config
from .exceptions import InvalidVideoIdException

PATTERN = re.compile(r"(.*)\(([0-9]+)\)$")

PATTERN_YTURL = re.compile(r"((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)")

YT_VIDEO_ID_LENGTH = 11

CLIENT_VERSION = ''.join(("2.", (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y%m%d"), ".01.00"))

UA = config.headers["user-agent"]


def extract(url):
    _session = requests.Session()
    html = _session.get(url, headers=config.headers)
    with open(str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                  ) + 'test.json', mode='w', encoding='utf-8') as f:
        json.dump(html.json(), f, ensure_ascii=False)


def save(data, filename, extention) -> str:
    save_filename = filename + "_" + \
        (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + extention
    with open(save_filename, mode='w', encoding='utf-8') as f:
        f.writelines(data)
    return save_filename


def checkpath(filepath):
    splitter = os.path.splitext(os.path.basename(filepath))
    body = splitter[0]
    extention = splitter[1]
    newpath = filepath
    counter = 1
    while os.path.exists(newpath):
        match = re.search(PATTERN, body)
        if match:
            counter = int(match[2]) + 1
            num_with_bracket = f'({str(counter)})'
            body = f'{match[1]}{num_with_bracket}'
        else:
            body = f'{body}({str(counter)})'
        newpath = os.path.join(os.path.dirname(filepath), body + extention)
    return newpath


def get_param(continuation, replay=False, offsetms: int = 0, dat=''):
    if offsetms < 0:
        offsetms = 0
    ret = {
        "context": {
            "client": {
                "visitorData": dat,
                "userAgent": UA,
                "clientName": "WEB",
                "clientVersion": CLIENT_VERSION,
            },

        },
        "continuation": continuation,
    }
    if replay:
        ret.setdefault("currentPlayerState", {
                       "playerOffsetMs": str(int(offsetms))})
    return ret


def extract_video_id(url_or_id: str) -> str:
    ret = ''
    if '[' in url_or_id:
        url_or_id = url_or_id.replace('[', '').replace(']', '')

    if type(url_or_id) != str:
        raise TypeError(f"{url_or_id}: URL or VideoID must be str, but {type(url_or_id)} is passed.")
    if len(url_or_id) == YT_VIDEO_ID_LENGTH:
        return url_or_id
    match = re.search(PATTERN_YTURL, url_or_id)
    if match is None:
        raise InvalidVideoIdException(f"Invalid video id: {url_or_id}")
    try:
        ret = match.group(4)
    except IndexError:
        raise InvalidVideoIdException(f"Invalid video id: {url_or_id}")

    if ret is None or len(ret) != YT_VIDEO_ID_LENGTH:
        raise InvalidVideoIdException(f"Invalid video id: {url_or_id}")
    return ret


def time_to_seconds(time_str):
    
    parts = list(map(int, str(time_str).split(':')))
    
    
    # "DD:HH:MM:SS"
    if len(parts) == 4:
        days, hours, minutes, seconds = parts
    # "HH:MM:SS"
    elif len(parts) == 3:
        days = 0
        hours, minutes, seconds = parts
    # "MM:SS"
    elif len(parts) == 2:
        days = 0
        hours = 0
        minutes, seconds = parts
    # "SS"
    elif len(parts) == 1:
        days = 0
        hours = 0
        minutes = 0
        seconds = parts[0]
    else:
        raise ValueError("Invalid time format: '" + time_str + "'")
        

    return days * 24*3600 + hours * 3600 + minutes * 60 + seconds