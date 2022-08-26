from asyncio import get_event_loop
from os import system, remove
from sys import argv

from aiohttp import ClientSession
from bilibili_api import Credential, video


async def getmov(vid: str):
    credential = Credential(sessdata="", bili_jct="", buvid3="")
    v = video.Video(vid, credential=credential)
    info = await v.get_info()
    url = await v.get_download_url(0)
    video_url = url["dash"]["video"][0]['baseUrl']
    audio_url = url["dash"]["audio"][0]['baseUrl']
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com/"
    }
    async with ClientSession() as sess:
        async with sess.get(video_url, headers=HEADERS) as resp:
            length = resp.headers.get('content-length')
            with open(argv[2] + '\\video_temp.m4s', 'wb') as f:
                process = 0
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    process += len(chunk)
                    print(f'下载视频流 {process} / {length}')
                    f.write(chunk)
        async with sess.get(audio_url, headers=HEADERS) as resp:
            length = resp.headers.get('content-length')
            with open(argv[2] + '\\audio_temp.m4s', 'wb') as f:
                process = 0
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    process += len(chunk)
                    print(f'下载音频流 {process} / {length}')
                    f.write(chunk)
    system(argv[3] + ' -i ' + argv[2] + '\\video_temp.m4s -i ' + argv[
        2] + '\\audio_temp.m4s \"' + argv[2] + '\\' + info['title'] + '.mp4\"')
    remove(argv[2] + '\\video_temp.m4s')
    remove(argv[2] + '\\audio_temp.m4s')


get_event_loop().run_until_complete(getmov(argv[1]))
