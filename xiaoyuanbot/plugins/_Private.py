# -*- coding: utf-8 -*-
from json import loads
from os import popen, system, path
from sys import argv
from urllib import parse

from requests import get, post

fpath = path.split(path.realpath(argv[0]))[0]


def translate(target):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36 '
    }

    req = get('http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=' + target, headers=headers)
    result = loads(req.text).get("translateResult")[0][0].get("tgt")
    return str(result)


def musicgetter(name):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.141 Safari/537.36 '
        }
        req = get('http://cloud-music.pl-fe.cn/search?keywords=' + name, headers=headers)
        if req.json().get("code") == 200:
            name = req.json().get("result").get("songs")[0].get("name")
            artist = req.json().get("result").get("songs")[0].get("artists")[0].get("name")
            musid = req.json().get("result").get("songs")[0].get("id")
            return [str(name), str(artist), str(musid)]
        else:
            return ['查询失败', '查询失败', '000000']
    except:
        return ['无法请求', '无法请求', '000000']


def bilibili_up(uid):
    try:
        url = "https://api.bilibili.com/x/relation/stat"
        params = {"vmid": uid, "jsonp": "jsonp"}
        res = get(url=url, params=params)
        js = eval(res.text)
        return js["data"]["mid"], js["data"]["following"], js["data"]["follower"], js["data"]["black"]
    except:
        return None, None, None, None


def covidgetter():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36 '
    }
    req = get('https://c.m.163.com/ug/api/wuhan/app/data/list-total', headers=headers)
    if loads(req.text).get("code") == 10000:
        confirm = loads(req.text).get("data").get("chinaTotal").get("today").get("confirm")
        heal = loads(req.text).get("data").get("chinaTotal").get("today").get("heal")
        dead = loads(req.text).get("data").get("chinaTotal").get("today").get("dead")
        return [str(confirm), str(heal), str(dead)]
    else:
        return ["获取失败", "获取失败", "获取失败"]


def weathergetter(city: str) -> str:
    host = 'http://wthrcdn.etouch.cn/weather_mini?city='
    url = host + parse.quote(city)
    r = get(url)
    jsons = loads(r.text)
    str = city + '的天气：\n'
    len = 0
    for i in jsons['data']['forecast']:
        if len < 2:
            if len == 0:
                str += '今日：'
            if len == 1:
                str += '明日：'
            str += i['date']
            str += '\n天气：'
            str += i['type']
            str += '\n最'
            str += i['low']
            str += '\n最'
            str += i['high']
            str += '\n'
            len += 1
    return str


def command_executor(command_t: str) -> str:
    f = popen(command_t, "r")
    d = f.read()
    print(d)
    f.close()
    if d:
        return d
    else:
        return f'指令错误或没有输出结果'


def makeGrass(text: str) -> str:
    ret = ''
    if not text.replace(' ', '').replace(',', '').replace('?', '').replace('!', '').replace('.,', '').replace('(',
                                                                                                              '').replace(
        ')', '').encode('utf-8').isalpha():
        text = translate(text)
    text_t = text.split(' ')
    for txt in text_t:
        ret = ret + translate(txt)
    return ret


def text2speach(text: str):
    post('http://www.mysqlschool.cn/SpeekText/index.php?type=2&text=' + text + '&voice_name=zh-CN-XiaoxiaoNeural')


def playmusic(file: str):
    system('taskkill /f /im ffplay.exe')
    system('start ' + fpath + '\\xiaoyuanbot\\plugins\\ffplay.exe ' + file)
