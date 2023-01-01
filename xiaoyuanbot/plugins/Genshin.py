from json import loads

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from requests import get

genshin = on_command('genshin')


@genshin.handle()
async def _(event: GroupMessageEvent):
    uuid = str(event.message).replace('genshin ', '')
    req = get('https://api.daidr.me/apis/genshinUserinfo?uid=' + uuid + '&server=0')
    js = loads(req.text)
    if not js['retcode'] == 0:
        await genshin.finish(js['message'])
    await genshin.finish('旅行者' + uuid + '的信息:\n' + '活跃天数: ' + str(
        js['data']['stats']['active_day_number']) + '\n成就达成数: ' + str(
        js['data']['stats']['achievement_number']) + '\n风神瞳: ' + str(
        js['data']['stats']['achievement_number']) + '\n岩神瞳: ' + str(
        js['data']['stats']['geoculus_number']) + '\n雷神瞳: ' + str(
        js['data']['stats']['electroculus_number']) + '\n草神瞳: ' + str(
        js['data']['stats']['dendroculus_number']) + '\n获得角色数: ' + str(
        js['data']['stats']['avatar_number']) + '\n解锁传送点: ' + str(
        js['data']['stats']['way_point_number']) + '\n解锁秘境: ' + str(
        js['data']['stats']['domain_number']) + '\n深境螺旋: ' + str(
        js['data']['stats']['spiral_abyss']) + '\n华丽宝箱数: ' + str(
        js['data']['stats']['luxurious_chest_number']) + '\n珍贵宝箱数: ' + str(
        js['data']['stats']['precious_chest_number']) + '\n精致宝箱数: ' + str(
        js['data']['stats']['exquisite_chest_number']) + '\n普通宝箱数: ' + str(
        js['data']['stats']['common_chest_number']) + '\n奇馈宝箱数: ' + str(js['data']['stats']['magic_chest_number']))
