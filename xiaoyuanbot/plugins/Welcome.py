# -*- coding: utf-8 -*-
from os import path
from random import choice
from sys import argv

from nonebot import on_notice, on_message, on_request
from nonebot.adapters.onebot.v11 import MessageSegment, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, \
    GroupAdminNoticeEvent, GroupUploadNoticeEvent, GroupMessageEvent, GroupBanNoticeEvent, FriendRequestEvent, \
    GroupRequestEvent, Bot

fpath = path.split(path.realpath(argv[0]))[0]
group_increase = on_notice()


@group_increase.handle()
async def _(event: GroupIncreaseNoticeEvent):
    await group_increase.finish(choice(
        ['很高兴遇见你,' + MessageSegment.at(event.user_id) + ',我们希望您给我们带份披萨',
         '你做到了!' + MessageSegment.at(event.user_id), '一只野生的' + MessageSegment.at(event.user_id) + '出现了',
         MessageSegment.at(event.user_id) + '跳进了群组']))


group_decrease = on_notice()


@group_decrease.handle()
async def _(bot: Bot, event: GroupDecreaseNoticeEvent):
    if event.sub_type == 'leave':
        user_info = await bot.call_api('get_stranger_info', user_id=event.user_id)
        await group_decrease.finish('@' + user_info["nickname"] + ' (' + str(event.user_id) + ')' + '离开了群组(leave)')
    else:
        user_info = await bot.call_api('get_stranger_info', user_id=event.user_id)
        await group_decrease.finish('@' + user_info["nickname"] + ' (' + str(event.user_id) + ')' + '离开了群组(kick)')


group_admin = on_notice()


@group_admin.handle()
async def _(event: GroupAdminNoticeEvent):
    if event.sub_type == 'set':
        await group_admin.finish(MessageSegment.at(event.user_id) + '已升职为管理员!')
    else:
        await group_admin.finish(MessageSegment.at(event.user_id) + '已被贬为平民!')


friend = on_request()


@friend.handle()
async def _(bot: Bot, event: FriendRequestEvent):
    await bot.set_friend_add_request(flag=event.flag, approve=True)


group = on_request()


@group.handle()
async def _(bot: Bot, event: GroupRequestEvent):
    if event.sub_type == 'invite':
        await bot.set_group_add_request(flag=event.flag, approve=True)


upload = on_notice()


@upload.handle()
async def _(bot: Bot, event: GroupUploadNoticeEvent):
    file = event.file
    url = await bot.call_api(api='get_group_file_url', group_id=event.group_id, file_id=file.id, busid=file.busid)
    with open(fpath + '\\xiaoyuanbot\\plugins\\Scanner.txt', 'w+') as f:
        f.write(url['url'])
        f.close()
    await group_admin.finish(
        '文件上传:\n文件名:' + file.name + '\n大小:' + str(file.size) + '字节\n上传者:' + MessageSegment.at(
            event.user_id))


message = on_message()


@message.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedMessage.txt', 'r', encoding='utf-8') as f:
        if not f.read().find(str(event.message)) == -1:
            f.close()
            await bot.delete_msg(message_id=event.message_id)
            await message.finish(MessageSegment.at(event.user_id) + ',你发送的消息里有管理员禁止发送的文本!')
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedUser.txt', 'r') as f:
        if not f.read().find(str(event.user_id)) == -1:
            f.close()
            await bot.delete_msg(message_id=event.message_id)
            await message.finish(MessageSegment.at(event.user_id) + '因为被管理员封锁而被拒绝发送消息!')


ban = on_notice()


@ban.handle()
async def _(event: GroupBanNoticeEvent):
    await group_admin.finish(MessageSegment.at(event.user_id) + '被管理员禁言' + str(event.time) + '秒!')
