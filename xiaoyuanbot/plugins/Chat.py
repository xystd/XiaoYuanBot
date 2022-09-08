# -*- coding: utf-8 -*-
from json import loads
from os import path
from sys import argv
from threading import Thread

from flask import Flask
from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot

sync = on_message()
fpath = path.split(path.realpath(argv[0]))[0]
app = Flask(__name__)
sync_group = open(fpath + '\\xiaoyuanbot\\plugins\\Syncgroup.txt', 'r').read()


def runapp():
    app.run(port=8088, host='0.0.0.0')


thr = Thread(target=runapp)
thr.start()


@app.route('/getchatmsg')
def _():
    with open(fpath + '\\xiaoyuanbot\\plugins\\Chat.txt', 'r', encoding='utf-8') as f:
        return f.read().encode('utf-8')


@sync.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\Chat.txt', 'w+', encoding='utf-8') as f:
        js = loads(event.json())
        f.write(js["sender"]["nickname"] + ': ' + str(event.get_message()))
        f.close()
        if not int(sync_group) == event.group_id:
            group_info = await bot.call_api('get_group_info', group_id=event.group_id)
            if not js["sender"]["card"] == '':
                await bot.send_group_msg(group_id=int(sync_group),
                                         message=str(group_info["group_name"]) + '(' + str(event.group_id) + ')@' +
                                                 js["sender"]["card"] + ' (' + str(event.user_id) + '):' + str(
                                             event.message))
            else:
                await bot.send_group_msg(group_id=int(sync_group),
                                         message=str(group_info["group_name"]) + '(' + str(event.group_id) + ')@' +
                                                 js["sender"]["nickname"] + ' (' + str(event.user_id) + '):' + str(
                                             event.message))
