# -*- coding: utf-8 -*-
from json import dump, dumps, loads
from os import path, mkdir
from random import seed, choice, randint
from sys import argv

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.permission import *

seed()
fpath = path.split(path.realpath(argv[0]))[0]
if not path.isdir(fpath + '\\xiaoyuanbot\\plugins\\Game'):
    mkdir(fpath + '\\xiaoyuanbot\\plugins\\Game')
duck = on_command('duck')


@duck.handle()
async def _(event: GroupMessageEvent):
    ducknum = str(event.message).split(" ")[1]
    ducknum = int(ducknum)
    if ducknum == 0:
        await duck.finish("下次游玩请输入数字")
    if ducknum > 30:
        await duck.finish("抓不到")
    else:
        await duck.send("抓到了")
        await duck.finish("噶" * ducknum)


greg = on_command('g-reg')


@greg.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    if not path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', 'w+') as f:
            data = {
                "Coal": 0,
                "Iron": 0,
                "Gold": 0,
                "Diamond": 0,
                "Oak": 0,
                "Acacia": 0,
                "Jungle": 0,
                "Dark_Oak": 0
            }
            f.write(dumps(data))
            f.close()
        await greg.finish('你已经成功注册,可以开始游戏')
    else:
        await greg.finish('你已经注册过了,请勿重复注册')


mine = on_command('mine')


@mine.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    item_t = choice(['煤炭', '铁矿', '金矿', '钻石', '空气'])
    item_s = randint(1, 64)
    with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
        js = loads(f.read())
        f.close()
    if item_t == '煤炭':
        js["Coal"] = js["Coal"] + item_s
    if item_t == '铁矿':
        js["Iron"] = js["Iron"] + item_s
    if item_t == '金矿':
        js["Gold"] = js["Gold"] + item_s
    if item_t == '钻石':
        js["Diamond"] = js["Diamond"] + item_s
    if item_t == '空气':
        item_s = 0
    if not item_t == '空气' and not item_s == '0':
        if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
            with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "w") as f:
                dump(js, f)
                f.close()
        else:
            await mine.finish('你没有注册,请输入\"g-reg\"来注册')
        await mine.finish('你挖到了' + str(item_s) + '个' + item_t)
    else:
        await mine.finish('你挖了个寂寞')


cut = on_command('cut')


@cut.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    item_t = choice(['橡木', '金合欢木', '丛林木', '深色橡木', '空气'])
    item_s = randint(1, 64)
    with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
        js = loads(f.read())
        f.close()
    if item_t == '橡木':
        js["Oak"] = js["Oak"] + item_s
    if item_t == '金合欢木':
        js["Acacia"] = js["Acacia"] + item_s
    if item_t == '丛林木':
        js["Jungle"] = js["Jungle"] + item_s
    if item_t == '深色橡木':
        js["Dark_Oak"] = js["Dark_Oak"] + item_s
    if item_t == '空气':
        item_s = 0
    if not item_t == '空气' and not item_s == '0':
        if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
            with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "w") as f:
                dump(js, f)
                f.close()
        else:
            await cut.finish('你没有注册,请输入\"g-reg\"来注册')
        await cut.finish('你砍到了' + str(item_s) + '个' + item_t)
    else:
        await cut.finish('你砍了个寂寞')


back = on_command('back')


@back.handle()
async def _(event: GroupMessageEvent):
    item = ''
    user_id = str(event.user_id)
    if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
            js = loads(f.read())
            f.close()
            if not js["Coal"] == 0:
                item = item + " " + str(js["Coal"]) + "个煤炭"
            if not js["Iron"] == 0:
                item = item + " " + str(js["Iron"]) + "个铁矿"
            if not js["Gold"] == 0:
                item = item + " " + str(js["Gold"]) + "个金矿"
            if not js["Diamond"] == 0:
                item = item + " " + str(js["Diamond"]) + "个钻石"
            if not js["Oak"] == 0:
                item = item + " " + str(js["Oak"]) + "个橡木"
            if not js["Acacia"] == 0:
                item = item + " " + str(js["Acacia"]) + "个金合欢木"
            if not js["Jungle"] == 0:
                item = item + " " + str(js["Jungle"]) + "个丛林木"
            if not js["Dark_Oak"] == 0:
                item = item + " " + str(js["Dark_Oak"]) + "个深色橡木"
            await back.finish('你有' + item)
            if js["Coal"] == 0 and js["Iron"] == 0 and not js["Gold"] == 0 and js["Diamond"] == 0 and js["Oak"] == 0 and \
                    js["Acacia"] == 0 and js["Jungle"] == 0 and js["Dark_Oak"] == 0:
                await back.finish('你没有任何物品')
    else:
        await back.finish('你没有注册,请输入\"g-reg\"来注册')


mdiam = on_command('m-diam')


@mdiam.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
            js = loads(f.read())
            f.close()
            if not js["Diamond"] == 0:
                Diamond = js["Diamond"]
                await mdiam.finish('你有' + str(Diamond) + '个钻石')
            else:
                await mdiam.finish('你没有钻石')
    else:
        await mdiam.finish('你没有注册,请输入\"g-reg\"来注册')


sign = on_command('sign')


@sign.handle()
async def _(event: GroupMessageEvent):
    user_id = str(event.user_id)
    diamond = randint(1, 64)
    with open(fpath + '\\xiaoyuanbot\\plugins\\Signed.txt', "r") as f:
        if not f.read().find(user_id) == -1:
            await sign.finish('你已经签过到了!')
        f.close()
    if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
            js = loads(f.read())
            f.close()
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "w") as f:
            js['Diamond'] = js['Diamond'] + diamond
            dump(js, f)
            f.close()
        with open(fpath + '\\xiaoyuanbot\\plugins\\Signed.txt', "a") as f:
            f.write(user_id + '\n')
            await sign.finish('签到成功,你获得了' + str(diamond) + '个钻石')
    else:
        await sign.finish('你没有注册,请输入\"g-reg\"来注册')


pvp = on_command('pvp')


@pvp.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    json = loads(event.json())
    user_id = str(event.user_id)
    diamond = int(str(event.message).replace('pvp ', ''))
    diamond_t = randint(1, diamond)
    ench_level = randint(1, 32767)
    weapons = ''
    hurt = 0
    hurt_t = randint(1, 8)
    if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "r") as f:
            js = loads(f.read())
            f.close()
        if js['Diamond'] >= diamond:
            if diamond >= 1:
                weapons = '木剑'
                hurt = 4
            if diamond >= 500:
                weapons = '石剑'
                hurt = 6
            if diamond >= 1000:
                weapons = '铁剑'
                hurt = 6
            if diamond >= 1000:
                weapons = '钻石剑'
                hurt = 8
            if diamond >= 3000:
                weapons = '下界合金剑'
                hurt = 8
            if diamond >= 5000:
                weapons = '下界合金剑,附魔效果:锋利 enchantment.level.' + str(ench_level)
                hurt = 8 + 0.5 * ench_level + 0.5
            if hurt > hurt_t:
                msg = [
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你获得了" + weapons
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你的伤害是:" + str(hurt)
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "对手的伤害是:" + str(hurt_t)
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "XiaoYuanBot被" + json["sender"]["nickname"] + "击杀 最终击杀!"
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你赢了!获得了" + str(diamond_t) + "个钻石!"
                        }
                    }
                ]
                with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "w") as f:
                    js['Diamond'] = js['Diamond'] - diamond
                    js['Diamond'] = js['Diamond'] + diamond_t
                    dump(js, f)
                    f.close()
                    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)
            else:
                msg = [
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你获得了" + weapons
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你的伤害是:" + str(hurt)
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "对手的伤害是:" + str(hurt_t)
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": json["sender"]["nickname"] + "被" + "XiaoYuanBot击杀 最终击杀!"
                        }
                    },
                    {
                        "type": "node",
                        "data": {
                            "name": "XiaoYuanBot",
                            "uin": bot.self_id,
                            "content": "你输了!你没有拿回一个钻石!"
                        }
                    }
                ]
                with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + user_id + '.json', "w") as f:
                    js['Diamond'] = js['Diamond'] - diamond
                    dump(js, f)
                    f.close()
                    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)
        else:
            await pvp.finish('你的钻石数不足以进行游戏!')
    else:
        await pvp.finish('你没有注册,请输入\"g-reg\"来注册')


edit = on_command('edit', permission=SUPERUSER)


@edit.handle()
async def _(event: GroupMessageEvent):
    if not str(event.message).find('[CQ:at,qq=') == -1:
        args = str(event.message).replace('edit [CQ:at,qq=', '').replace(']', '').replace(' ', '').split(",")
    else:
        args = str(event.message).replace('edit ', '').split(",")
    if path.isfile(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + args[0] + '.json'):
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + args[0] + '.json', "r") as f:
            js = loads(f.read())
            f.close()
        with open(fpath + '\\xiaoyuanbot\\plugins\\Game\\' + args[0] + '.json', "w") as f:
            js['Diamond'] = int(args[1])
            dump(js, f)
            f.close()
            await edit.finish('钻石数修改成功!')
    else:
        await pvp.finish('该用户尚未注册')
