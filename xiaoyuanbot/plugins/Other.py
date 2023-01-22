# -*- coding: utf-8 -*-
from os import path
from random import seed, choice, randint
from sys import argv
from time import strftime

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


splashes = on_command('splashes')


@splashes.handle()
async def _():
    if strftime("%m%d") == "1109":
        await splashes.finish('Happy birthday, ez!')
    if strftime("%m%d") == "0601":
        await splashes.finish('Happy birthday, Notch!')
    if strftime("%m%d") == "1224":
        await splashes.finish('Merry X-mas!')
    if strftime("%m%d") == "0101":
        await splashes.finish('Happy new year!')
    if strftime("%m%d") == "1031":
        await splashes.finish('OOoooOOOoooo! Spooky!')
    with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\Splashes.txt', "r") as f:
        spl = f.read().split("\n")
        await splashes.finish(spl[randint(0, len(spl))])
