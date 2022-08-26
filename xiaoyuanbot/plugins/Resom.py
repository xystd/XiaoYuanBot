# -*- coding: utf-8 -*-
from os import path
from random import randint
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment, Bot

fpath = path.split(path.realpath(argv[0]))[0]

menu = on_command('menu')


@menu.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = [
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "---------命令菜单----------"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "menu -- 显示这条信息"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "echo -- (NoneBot内置插件,需要@机器人),输出一段文本,用法:echo <文本>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "covid -- 每日疫情信息"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "fmusic -- 查找音乐,用法:fmusic <音乐名>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "fakemsg -- 制造假消息,用法:fakemsg <QQ号>,<昵称>,<消息>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "ping -- 测试一个网络地址是否畅通,用法:ping <网络地址>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "play -- 以发送语音的形式播放音乐,用法:play <音乐名>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "makeqr -- 制作一个二维码,用法:makeqr <想要写进二维码的文本/网址>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "r-pic -- 随机二刺螈图片"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "r-mcpic -- 随机MC图片(末影人)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "speak -- 以发送语音的形式说一句话,用法:speak <文本>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "timenow -- 显示现在的时间"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "fanyi -- 翻译一段文本,用法:fanyi <文本>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "weather -- 查询今天的天气,用法:weather <地区>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "yxh -- 用营销号的语气创建一段文本,用法:yxh <名字>,<事件>,<另一种说法>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "nice -- 发送随机Nice爷爷表情包"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "surprise -- 惊喜(你绝对想不到)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "mkgrass -- 使用生草翻译翻译一段文本,用法:mkgrass <文本>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "bili -- 查询B站视频信息,用法:bili <AV号/BV号>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "sync -- 设置当前群聊为聊天转发群(需要超级用户权限)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "此刻人品:" + str(randint(0, 100))
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "------------------------"
            }
        }
    ]
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)


amenu = on_command('a-menu')


@amenu.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = [
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "---------管理菜单----------"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "kick -- 踢出一个人,用法:kick <@某人>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "ban -- 禁言一个人,用法:ban <@某人\\全体成员>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "unban -- 解除禁言一个人,用法:unban <@某人\\全体成员>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "admin -- 将一个人设置为管理员,用法:admin <@某人>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "unadmin -- 取消一个人的管理员身份,用法:unadmin <@某人>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "title -- 给一个人设置特殊头衔,用法:title <@某人> <头衔>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "msgban -- 封禁一条消息,用法:msgban <消息>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "msgunban -- 解除封禁一条消息,用法:msgunban <消息>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "block -- 封锁一个用户,用法:block <@用户名\\QQ号>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "unblock -- 解除封锁一个用户,用法:unblock <@用户名\\QQ号>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "此刻人品:" + str(randint(0, 100))
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "------------------------"
            }
        }
    ]
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)


gmenu = on_command('g-menu')


@gmenu.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = [
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "---------游戏菜单----------"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "duck -- 抓鸭子游戏,玩法:duck <鸭子只数>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "g-reg -- 注册所有要注册的游戏"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "mine -- 模拟挖矿(灵感来源:Minecraft,需要使用\"g-reg\"注册)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "cut -- 模拟撸树(灵感来源:Minecraft,需要使用\"g-reg\"注册)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "back -- 显示背包物品(需要先游玩以上游戏)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "m-diam -- 显示您持有的钻石数(需要先游玩以上游戏)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "sign -- 每日签到(需要使用\"g-reg\"注册)"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "pvp -- 模拟PvP(灵感来源:Hypixel,需要使用\"g-reg\"注册),用法:pvp <你要赌出去的钻石数>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "edit -- 修改钻石数(需要超级用户权限),用法:edit <QQ号>,<要设置的钻石数>"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "此刻人品:" + str(randint(0, 100))
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "------------------------"
            }
        }
    ]
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)


smenu = on_command('s-menu')


@smenu.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = [
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "---" + MessageSegment.face(16) + "Beluga Heck Tools Menu" + MessageSegment.face(16) + "---"
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "heck -- Heck in other's phone and get something."
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "password -- Change password. "
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "power -- Give others heck power."
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "paswd -- Enter the root password."
            }
        },
        {
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "----------------------------------------------"
            }
        }
    ]
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)


cmenu = on_command('c-menu')


@cmenu.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\Syncgroup.txt', 'r') as f:
        if f.read() == str(event.group_id):
            f.close()
            msg = [
                {
                    "type": "node",
                    "data": {
                        "name": "XiaoYuanBot",
                        "uin": bot.self_id,
                        "content": "--------聊天转发群专属菜单---------"
                    }
                },
                {
                    "type": "node",
                    "data": {
                        "name": "XiaoYuanBot",
                        "uin": bot.self_id,
                        "content": "send -- 发送一条消息,用法:send <--Private\\--Group> <群号>,<消息>"
                    }
                }
            ]
            await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)
