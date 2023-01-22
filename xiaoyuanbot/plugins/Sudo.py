# -*- coding: utf-8 -*-
from os import path
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from requests import get

from ._Private import command_executor

fpath = path.split(path.realpath(argv[0]))[0]
passed = False
sudo = on_command('sudo')


@sudo.handle()
async def _(event: GroupMessageEvent):
    args = str(event.message).split(" ")
    if args[1] == 'heck':
        if not str(event.message).find('[CQ:at,qq=') == -1:
            user_id = str(event.message).replace('sudo heck [CQ:at,qq=', '').replace(']', '')
        else:
            user_id = str(event.message).replace('sudo heck ', '')
        with open(fpath + '\\xiaoyuanbot\\plugins\\Powered.txt', 'r') as f:
            if f.read().find(str(event.user_id)) == -1:
                f.close()
                await sudo.finish('You don\'t know how to heck yet!')
        if passed:
            req = get("https://zy.xywlapi.cc/qqapi?qq=" + user_id)
            if req.json().get("status") == 200:
                await sudo.finish(
                    str('Heck finished,return:Get phone number finished,the phone number is ' + req.json().get(
                        "phone")) + '!')
            else:
                await sudo.finish(str('Heck finished,return:Nothing for you:)'))
        else:
            await sudo.send('Please use \"paswd\" to enter the root password at first!')
    if args[1] == 'power':
        user_id = str(event.message).replace('sudo power [CQ:at,qq=', '').replace(']', '')
        with open(fpath + '\\xiaoyuanbot\\plugins\\Powered.txt', 'r') as f:
            if f.read().find(str(event.user_id)) == -1:
                f.close()
                await sudo.finish('You don\'t know how to heck yet!')
            if f.read().find(str(user_id)) != -1:
                f.close()
                await sudo.finish('He has been powered!')
        if passed:
            with open(fpath + '\\xiaoyuanbot\\plugins\\Powered.txt', 'a') as f:
                f.write('\n' + user_id)
                f.close()
                await sudo.finish(
                    MessageSegment.at(int(user_id)) + ' had powered by ' + MessageSegment.at(event.user_id) + '!')
        else:
            await sudo.send('Please use \"paswd\" to enter the root password at first!')
    if not args[1] == 'heck' and not args[1] == 'power':
        command = str(event.message).replace('sudo ', '')
        with open(fpath + '\\xiaoyuanbot\\plugins\\Powered.txt', 'r') as f:
            if f.read().find(str(event.user_id)) == -1:
                f.close()
                await sudo.finish('You don\'t know how to heck yet!')
        if passed:
            await sudo.finish(command_executor(command))
        else:
            await sudo.send('Please use \"paswd\" to enter the root password at first!')


paswd = on_command('paswd')


@paswd.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    password = str(event.message).replace('paswd ', '')
    with open(fpath + '\\xiaoyuanbot\\plugins\\Powered.txt', 'r') as f:
        if f.read().find(user_id) != -1:
            f.close()
            if password == 'Beluga#0001':
                global passed
                passed = True
                await paswd.finish('You are passed to use heck tools!')
        else:
            f.close()
            await paswd.finish('You don\'t know how to heck yet!')
