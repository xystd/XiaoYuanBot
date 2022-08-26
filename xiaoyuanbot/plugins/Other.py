# -*- coding: utf-8 -*-
from os import path
from random import seed, choice
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment

seed()
fpath = path.split(path.realpath(argv[0]))[0]
nice = on_command('nice')


@nice.handle()
async def _():
    await nice.finish(MessageSegment.image(
        f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\' + choice(['Nice.png', 'Nice.jpg', 'Nice.gif'])))


surprise = on_command('surprise')


@surprise.handle()
async def _():
    await surprise.finish(MessageSegment.record(
        f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\' + choice(['Rick.amr', 'Carol.amr', '13.amr'])))
