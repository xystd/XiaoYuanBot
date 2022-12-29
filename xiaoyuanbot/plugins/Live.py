# -*- coding: utf-8 -*-
from os import path, remove
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from playsound import playsound
from requests import get

from ._Private import musicgetter

fpath = path.split(path.realpath(argv[0]))[0]

liveplay = on_command('live-play')


@liveplay.handle()
async def _(event: GroupMessageEvent):
    name = str(event.message).replace('live-play ', '')
    music = musicgetter(name)
    file = get(f'http://music.163.com/song/media/outer/url?id=' + music[2])
    with open(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3', 'wb') as f:
        f.write(file.content)
        f.close()
    await liveplay.send('正在播放:' + music[1] + ' - ' + music[0] + '\nhttps://music.163.com/song?id=' + music[2])
    playsound(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3')
    remove(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3')
