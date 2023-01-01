# -*- coding: utf-8 -*-
from os import path, system
from sys import argv

from bilibili_api import video, Credential
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from requests import get

from ._Private import musicgetter

fpath = path.split(path.realpath(argv[0]))[0]

liveplay = on_command('live-play')


@liveplay.handle()
async def _(event: GroupMessageEvent):
    name = str(event.message).replace('live-play ', '')
    music = musicgetter(name)
    file = get(f'http://music.163.com/song/media/outer/url?id=' + music[2])
    system('taskkill /f /im ffplay.exe')
    with open(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3', 'wb') as f:
        f.write(file.content)
        f.close()
    await liveplay.send('正在播放: ' + music[1] + ' - ' + music[0] + '\nhttps://music.163.com/song?id=' + music[2])
    system('start ' + fpath + '\\xiaoyuanbot\\plugins\\ffplay.exe ' + fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3')


liveplaymov = on_command('live-playmov')


@liveplaymov.handle()
async def _(event: GroupMessageEvent):
    vid = str(event.message).replace('live-playmov ', '')
    credential = Credential(sessdata="", bili_jct="", buvid3="")
    v = video.Video(vid, credential=credential)
    info = await v.get_info()
    system('taskkill /f /im ffplay.exe')
    system(
        fpath + '\\xiaoyuanbot\\plugins\\_Getmov.py ' + vid + ' \"' + fpath + '\\xiaoyuanbot\\plugins' + '\" \"' + fpath + '\\xiaoyuanbot\\plugins\\ffmpeg.exe\"')
    await liveplaymov.send('正在播放: ' + info['title'])
    system('start ' + fpath + '\\xiaoyuanbot\\plugins\\ffplay.exe ' + fpath + '\\xiaoyuanbot\\plugins\\' + info[
        'title'] + '.mp4')
