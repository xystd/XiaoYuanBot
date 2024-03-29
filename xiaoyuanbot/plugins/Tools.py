# -*- coding: utf-8 -*-
from json import loads
from os import path, remove, system
from sys import argv
from time import strftime

from bilibili_api import video, Credential
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.permission import *
from qrcode import make
from requests import get

from ._Private import command_executor, covidgetter, musicgetter, weathergetter, translate, makeGrass

fpath = path.split(path.realpath(argv[0]))[0]
covid = on_command('covid')


@covid.handle()
async def _():
    await covid.finish(
        "----国内疫情统计----\n今日确诊: " + covidgetter()[0] + "\n今日治愈: " + covidgetter()[1] + "\n今日死亡: " +
        covidgetter()[2])


fakemsg = on_command('fakemsg')


@fakemsg.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    args = str(event.message).replace('fakemsg ', '').replace('--NoInfo ', '').split(";")
    js = loads(event.json())
    msg = []
    for argi in args:
        arg = argi.split(",")
        msg.append({
            "type": "node",
            "data": {
                "name": arg[1],
                "uin": arg[0],
                "content": arg[2]
            }
        })
    if not str(event.message).find('--NoInfo '):
        msg.append({
            "type": "node",
            "data": {
                "name": "XiaoYuanBot",
                "uin": bot.self_id,
                "content": "此消息由@" + str(js["sender"]["nickname"]) + " 伪造的, 意味着这条消息并不存在, 请不要当真"
            }
        })
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg)
    await fakemsg.finish()


ping = on_command('ping')


@ping.handle()
async def _(event: GroupMessageEvent):
    address = str(event.message).replace('ping ', '')
    address = address.replace('>', '')
    address = address.replace('&', '')
    address = address.replace('|', '')
    returner = command_executor('ping ' + address)
    await ping.finish(returner)


play = on_command('play')


@play.handle()
async def _(event: GroupMessageEvent):
    name = str(event.message).replace('play ', '')
    music = musicgetter(name)
    file = get(f'http://music.163.com/song/media/outer/url?id=' + music[2])
    with open(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3', 'wb') as f:
        f.write(file.content)
        f.close()
    await play.send('正在播放: ' + music[1] + ' - ' + music[0] + '\nhttps://music.163.com/song?id=' + music[2])
    await play.send(MessageSegment.record(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\PlayMusic.mp3')
    await play.finish()


makeqr = on_command('makeqr')


@makeqr.handle()
async def _(event: GroupMessageEvent):
    text = str(event.message).replace('makeqr ', '')
    img = make(text)
    with open(fpath + '\\xiaoyuanbot\\plugins\\QRCode.png', 'wb') as f:
        img.save(f)
        f.close()
    await makeqr.send(MessageSegment.image(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\QRCode.png'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\QRCode.png')
    await makeqr.finish()


rpic = on_command('r-pic')


@rpic.handle()
async def _():
    await rpic.finish(MessageSegment.image('https://api.ixiaowai.cn/api/api.php'))


rr18pic = on_command('r-r18pic')


@rr18pic.handle()
async def _():
    with open(fpath + '\\xiaoyuanbot\\plugins\\RandomR18Picture.png', 'wb') as f:
        f.write(get('http://www.acy.moe/api/r18').content)
        f.close()
    system(
        fpath + '\\xiaoyuanbot\\plugins\\_Rickpic.py ' + fpath + '\\xiaoyuanbot\\plugins\\Rick.png ' + fpath + '\\xiaoyuanbot\\plugins\\RandomR18Picture.png ' + fpath + '\\xiaoyuanbot\\plugins\\Picture.png')
    await rr18pic.send(MessageSegment.image(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\Picture.png'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\RandomR18Picture.png')
    remove(fpath + '\\xiaoyuanbot\\plugins\\Picture.png')
    await rr18pic.finish()


rmcpic = on_command('r-mcpic')


@rmcpic.handle()
async def _():
    await rmcpic.finish(MessageSegment.image('https://api.ixiaowai.cn/mcapi/mcapi.php'))


rerrpic = on_command('r-errpic')


@rerrpic.handle()
async def _():
    await rerrpic.finish(MessageSegment.image('https://www.acy.moe/api/404'))


speak = on_command('speak')


@speak.handle()
async def _(event: GroupMessageEvent):
    text = str(event.message).replace('speak ', '')
    system(
        fpath + '\\xiaoyuanbot\\plugins\\Balcon\\balcon.exe -w ' + fpath + '\\xiaoyuanbot\\plugins\\SpeakAudio.wav -t '
                                                                           '\"' + text + '\"')
    await speak.send(MessageSegment.record(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\SpeakAudio.wav'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\SpeakAudio.wav')


timenow = on_command('timenow')


@timenow.handle()
async def _():
    time_now = strftime("%F %A %H:%M:%S")
    await timenow.finish("现在时间是: " + time_now)


fanyi = on_command('fanyi')


@fanyi.handle()
async def _(event: GroupMessageEvent):
    tsrc = str(event.message).replace('fanyi ', '')
    await fanyi.finish('翻译源: ' + tsrc + '\n翻译结果: ' + translate(tsrc))


weather = on_command('weather')


@weather.handle()
async def _(event: GroupMessageEvent):
    city = str(event.message).replace('weather ', '')
    await weather.finish(
        "----天气查询----\n地区: " + city + "\n最高指数: " + weathergetter(city)[0] + "\n最低指数: " +
        weathergetter(city)[
            1] + "\n天气: " + weathergetter(city)[2])


yxh = on_command('yxh')


@yxh.handle()
async def _(event: GroupMessageEvent):
    args = str(event.message).replace('yxh ', '').split(",")
    a = args[0]
    b = args[1]
    c = args[2]
    with open(fpath + '\\xiaoyuanbot\\plugins\\SSML_Xiaoxiao.xml', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = text.replace('XXX',
                            a + b + '是怎么回事呢？' + a + '相信大家都很熟悉，但是' + a + b + '是怎么回事呢，下面就让小编带大家一起了解吧。' + a + b + '，其实就是' + c + '，大家可能会很惊讶' + a + '怎么会' + b + '呢？但事实就是这样，小编也感到非常惊讶。这就是关于' + a + b + '的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！')
        file = open(fpath + '\\xiaoyuanbot\\plugins\\SSML.xml', 'w', encoding='UTF-8')
        file.write(text)
        f.close()
        file.close()
    system(
        fpath + '\\xiaoyuanbot\\plugins\\_Gettts.py --input ' + fpath + '\\xiaoyuanbot\\plugins\\SSML.xml --output ' + fpath + '\\xiaoyuanbot\\plugins\\YxhVoice')
    system(
        fpath + '\\xiaoyuanbot\\plugins\\ffmpeg.exe -i ' + fpath + '\\xiaoyuanbot\\plugins\\YxhVoice.mp3 -i ' + fpath + '\\xiaoyuanbot\\plugins\\YxhMusic.mp3 -filter_complex amix=inputs=2:duration=first:dropout_transition=2 -y -f mp3 ' + fpath + '\\xiaoyuanbot\\plugins\\YxhAudio.mp3')
    await yxh.send(MessageSegment.record(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\YxhAudio.mp3'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\SSML.xml')
    remove(fpath + '\\xiaoyuanbot\\plugins\\YxhVoice.mp3')
    remove(fpath + '\\xiaoyuanbot\\plugins\\YxhAudio.mp3')


film = on_command('film')


@film.handle()
async def _(event: GroupMessageEvent):
    args = str(event.message).replace('film ', '').split(",")
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    with open(fpath + '\\xiaoyuanbot\\plugins\\SSML_Yunxi.xml', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = text.replace('XXX',
                            '注意看，你眼前这个男人名叫' + a + '，他正在' + d + '，不料却被' + b + '发现，别眨眼，' + a + '赶紧去找，' + c + '，却发现' + c + '也被' + b + '发现，' + a + '不知道跑了多远，终于跑出了这里。其实我们都是电影里的每个人，遇到困难也不要退缩，勇敢超越自我，才能迎来人生的春天。这里是' + a + '说电影，关注我获得更多电影解说。')
        file = open(fpath + '\\xiaoyuanbot\\plugins\\SSML.xml', 'w', encoding='UTF-8')
        file.write(text)
        f.close()
        file.close()
    system(
        fpath + '\\xiaoyuanbot\\plugins\\_Gettts.py --input ' + fpath + '\\xiaoyuanbot\\plugins\\SSML.xml --output ' + fpath + '\\xiaoyuanbot\\plugins\\FilmVoice')
    system(
        fpath + '\\xiaoyuanbot\\plugins\\ffmpeg.exe -i ' + fpath + '\\xiaoyuanbot\\plugins\\FilmVoice.mp3 -i ' + fpath + '\\xiaoyuanbot\\plugins\\FilmMusic.mp3 -filter_complex amix=inputs=2:duration=first:dropout_transition=2 -y -f mp3 ' + fpath + '\\xiaoyuanbot\\plugins\\FilmAudio.mp3')
    await film.send(MessageSegment.record(f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\FilmAudio.mp3'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\SSML.xml')
    remove(fpath + '\\xiaoyuanbot\\plugins\\FilmVoice.mp3')
    remove(fpath + '\\xiaoyuanbot\\plugins\\FilmAudio.mp3')


mkgrass = on_command('mkgrass')


@mkgrass.handle()
async def _(event: GroupMessageEvent):
    text = str(event.message).replace('mkgrass ', '')
    text_new = makeGrass(text)
    await mkgrass.finish('生草翻译结果: ' + text_new)


bili = on_command('bili')


@bili.handle()
async def _(event: GroupMessageEvent):
    vid = str(event.message).replace('bili ', '')
    credential = Credential(sessdata="", bili_jct="", buvid3="")
    v = video.Video(vid, credential=credential)
    info = await v.get_info()
    file = get(info['pic'])
    with open(fpath + '\\xiaoyuanbot\\plugins\\CoverPicture.jpg', 'wb') as f:
        f.write(file.content)
        f.close()
    await bili.send(
        str(vid) + "的视频信息:\n" + "标题: " + info['title'] + "\nBv号: " + info['bvid'] + "\nAv号: " + "AV" + str(
            info['aid']) + "\n简介: " +
        info['desc'] + "\n发布者: " + info['owner']['name'] + "(" + str(
            info['owner']['mid']) + ")" + "\n播放量: " + str(
            info['stat']['view']) + "\n点赞: " +
        str(info['stat']['like']) + "\n投币: " + str(info['stat']['coin']) + "\n收藏: " + str(
            info['stat']['favorite']) + "\n封面: " + MessageSegment.image(
            f'file:///' + fpath + '\\xiaoyuanbot\\plugins\\CoverPicture.jpg'))
    remove(fpath + '\\xiaoyuanbot\\plugins\\CoverPicture.jpg')


playmov = on_command('playmov')


@playmov.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    vid = str(event.message).replace('playmov ', '')
    credential = Credential(sessdata="", bili_jct="", buvid3="")
    v = video.Video(vid, credential=credential)
    info = await v.get_info()
    system(
        fpath + '\\xiaoyuanbot\\plugins\\_Getmov.py ' + vid + ' \"' + fpath + '\\xiaoyuanbot\\plugins' + '\" \"' + fpath + '\\xiaoyuanbot\\plugins\\ffmpeg.exe\"')
    await bot.call_api('upload_group_file', group_id=event.group_id,
                       file=fpath + '\\xiaoyuanbot\\plugins\\' + info['title'] + '.mp4', name=info['title'] + '.mp4')
    remove(fpath + '\\xiaoyuanbot\\plugins\\' + info['title'] + '.mp4')


sync = on_command('sync', permission=SUPERUSER)


@sync.handle()
async def _(event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\Syncgroup.txt', 'w') as f:
        f.write(str(event.group_id))
        f.close()
        await sync.finish('此群已成为默认聊天转发群, 请重新启动Bot生效!')


send = on_command('send')


@send.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    with open(fpath + '\\xiaoyuanbot\\plugins\\Syncgroup.txt', 'r') as f:
        if f.read() == str(event.group_id):
            f.close()
            if str(event.message).find('send --Private') == -1 and str(event.message).find('send --Group') == -1:
                await send.finish('无效参数, 需要参数--Private或--Group')
            if not str(event.message).find('send --Private ') == -1:
                args = str(event.message).replace('send --Private ', '').split(",")
                if args[0] == 'msg':
                    msg = args[2]
                if args[0] == 'at':
                    msg = MessageSegment.at(int(args[2]))
                if args[0] == 'tts':
                    system(
                        fpath + '\\xiaoyuanbot\\plugins\\Balcon\\balcon.exe -w ' + fpath + '\\xiaoyuanbot\\plugins\\YxhAudio.wav -t \"' +
                        args[2] + '\"')
                if args[0] == 'xml':
                    msg = MessageSegment.xml(args[2])
                await bot.send_private_msg(user_id=int(args[1]), message=args[2])
                await send.finish('消息发送成功!')
            if not str(event.message).find('send --Group ') == -1:
                args = str(event.message).replace('send --Group ', '').split(",")
                if args[0] == 'msg':
                    msg = args[2]
                if args[0] == 'at':
                    msg = MessageSegment.at(int(args[2]))
                if args[0] == 'tts':
                    system(
                        fpath + '\\xiaoyuanbot\\plugins\\Balcon\\balcon.exe -w ' + fpath + '\\xiaoyuanbot\\plugins\\YxhAudio.wav -t \"' +
                        args[2] + '\"')
                if args[0] == 'xml':
                    msg = MessageSegment.xml(args[2])
                await bot.send_group_msg(group_id=int(args[1]), message=msg)
                remove(fpath + '\\xiaoyuanbot\\plugins\\SpeakAudio.wav')
                await send.finish('消息发送成功!')


mc = on_command('mc')


@mc.handle()
async def _(event: GroupMessageEvent):
    address = str(event.message).replace('mc ', '')
    if not address.find(':') == -1:
        addr = address.split(':')
        req = get('https://api.wer.plus/api/mcse?host=' + addr[0] + '&port=' + addr[1])
    else:
        req = get('https://api.wer.plus/api/mcse?host=' + address)
    if req.json().get("msg") == 'success':
        await mc.finish('服务器' + address + '当前的状态: 在线\n版本号: ' + req.json().get("data").get(
            "ver_name") + '\n服务器名称: ' + req.json().get("data").get("serv_name") + '\n在线人数: ' + req.json().get(
            "data").get(
            "onl_l") + '\n最多在线人数: ' + req.json().get("data").get("max_l") + '\n延迟: ' + req.json().get(
            "data").get(
            "serv_ping"))
    else:
        await mc.finish('服务器' + address + '当前的状态: 离线')
