# -*- coding: utf-8 -*-
from os import path
from random import randint
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.adapters.onebot.v11.permission import *

fpath = path.split(path.realpath(argv[0]))[0]
kick = on_command('kick', permission=GROUP_ADMIN | GROUP_OWNER)


@kick.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    user_id = str(event.message).replace('kick [CQ:at,qq=', '').replace(']', '')
    group_id = event.group_id
    await bot.set_group_kick(group_id=group_id, user_id=int(user_id))
    await kick.finish('已将' + MessageSegment.at(event.user_id) + '移出群组!')


ban = on_command('ban', permission=GROUP_ADMIN | GROUP_OWNER)


@ban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    user_id = str(event.message).replace('ban [CQ:at,qq=', '').replace(']', '')
    group_id = event.group_id
    if user_id == 'all':
        await bot.set_group_whole_ban(group_id=group_id, enable=True)
        await ban.finish('已设置全员禁言!')
    else:
        await bot.set_group_ban(group_id=group_id, user_id=int(user_id), duration=randint(1, 2591999))
        await ban.finish('已将' + MessageSegment.at(event.user_id) + '禁言随机时长!')


unban = on_command('unban', permission=GROUP_ADMIN | GROUP_OWNER)


@unban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    user_id = str(event.message).replace('unban [CQ:at,qq=', '').replace(']', '')
    group_id = event.group_id
    if user_id == 'all':
        await bot.set_group_whole_ban(group_id=group_id, enable=False)
        await unban.finish('已取消全员禁言!')
    else:
        await bot.set_group_ban(group_id=group_id, user_id=int(user_id), duration=0)
        await unban.finish('已取消禁言' + MessageSegment.at(event.user_id) + '!')


admin = on_command('admin', permission=GROUP_ADMIN | GROUP_OWNER)


@admin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    user_id = str(event.message).replace('admin [CQ:at,qq=', '').replace(']', '')
    group_id = event.group_id
    await bot.set_group_admin(group_id=group_id, user_id=int(user_id), enable=True)
    await admin.finish(MessageSegment.at(event.user_id) + '已被设为管理员!')


unadmin = on_command('unadmin', permission=GROUP_ADMIN | GROUP_OWNER)


@unadmin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    user_id = str(event.message).replace('unadmin [CQ:at,qq=', '').replace(']', '')
    group_id = event.group_id
    await bot.set_group_admin(group_id=group_id, user_id=int(user_id), enable=False)
    await unadmin.finish(MessageSegment.at(event.user_id) + '已被取消管理员!')


title = on_command('title', permission=GROUP_ADMIN | GROUP_OWNER)


@title.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    args = str(event.message).split(" ")
    user_id = args[1].replace('[CQ:at,qq=', '').replace(']', '')
    special_title = args[2]
    group_id = event.group_id
    await bot.set_group_special_title(group_id=group_id, user_id=int(user_id), special_title=special_title)
    await title.finish(MessageSegment.at(event.user_id) + '被给予专属头衔\"' + special_title + '\"')


msgban = on_command('msgban', permission=GROUP_ADMIN | GROUP_OWNER)


@msgban.handle()
async def _(event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedMessage.txt', 'a', encoding='utf-8') as f:
        f.write(str(event.message).replace('msgban ', '') + '\n')
        f.close()
        await msgban.finish('消息封禁成功!')


msgunban = on_command('msgunban', permission=GROUP_ADMIN | GROUP_OWNER)


@msgunban.handle()
async def _(event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedMessage.txt', 'w', encoding='utf-8') as f:
        f.write(f.read().replace(str(event.message).replace('msgunban ', ''), ''))
        f.close()
        await msgunban.finish('消息解除封禁成功!')


block = on_command('block', permission=GROUP_ADMIN | GROUP_OWNER)


@block.handle()
async def _(event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedUser.txt', 'a') as f:
        if not str(event.message).find('[CQ:at,qq=') == -1:
            user_id = str(event.message).replace('block [CQ:at,qq=', '').replace(']', '')
        else:
            user_id = str(event.message).replace('block ', '')
        f.write(user_id + '\n')
        f.close()
        await block.finish('用户封禁成功!')


unblock = on_command('unblock', permission=GROUP_ADMIN | GROUP_OWNER)


@unblock.handle()
async def _(event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\BannedUser.txt', 'w') as f:
        if not str(event.message).find('[CQ:at,qq=') == -1:
            user_id = str(event.message).replace('unblock [CQ:at,qq=', '').replace(']', '')
        else:
            user_id = str(event.message).replace('unblock ', '')
        f.write(f.read().replace(user_id, ''))
        f.close()
        await unblock.finish('用户解除封禁成功!')
