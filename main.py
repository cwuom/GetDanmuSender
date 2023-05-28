# -*- coding: utf-8 -*-

import ctypes
import math
import inspect
import os
import random
import re
from threading import Thread

import requests
import time
import json
import keyboard

import bili_pb2

"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
B站弹幕解析，支持解析番剧/分P视频/普通视频的全部弹幕并反推发送者UID

如何使用？
1. 程序在运行时会检测cookies可用性。请不要使用代理，这可能会让你无法通过cookies验证
2. 直接复制视频/番剧URL回车执行解析操作...

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
bilibili@im-cwuom(uid:473400804)
follow to get more
"""

# 保证每一次运行headers都不一样
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]
headers = {'User-Agent': random.choice(user_agent_list)}

crack_list = []  # 逆向mid后的弹幕数据
all_danmu = []  # 全部弹幕数据
tlist = []  # 存储逆向线程，用于提前终止逆向操作
STOP_FLAG = False  # 终止标签
gf = 0  # 写入检索弹幕并逆向mid后的结果

# ==================== output-log ====================
# You must initialize logging, otherwise you'll not see debug output.
# http.client.HTTPConnection.debuglevel = 1
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

# ==================== crc32-crack ====================
# from - https://github.com/Aruelius/crc32-crack
# DO NOT EDIT

CRCPOLYNOMIAL = 0xEDB88320
crctable = [0 for x in range(256)]


def create_table():
    for i in range(256):
        crcreg = i
        for _ in range(8):
            if (crcreg & 1) != 0:
                crcreg = CRCPOLYNOMIAL ^ (crcreg >> 1)
            else:
                crcreg = crcreg >> 1
        crctable[i] = crcreg


def crc32(string):
    crcstart = 0xFFFFFFFF
    for i in range(len(str(string))):
        index = (crcstart ^ ord(str(string)[i])) & 255
        crcstart = (crcstart >> 8) ^ crctable[index]
    return crcstart


def crc32_last_index(string):
    crcstart = 0xFFFFFFFF
    for i in range(len(str(string))):
        index = (crcstart ^ ord(str(string)[i])) & 255
        crcstart = (crcstart >> 8) ^ crctable[index]
    return index


def get_crc_index(t):
    for i in range(256):
        if crctable[i] >> 24 == t:
            return i
    return -1


def deep_check(i, index):
    string = ""
    hashcode = crc32(i)
    tc = hashcode & 0xff ^ index[2]
    if not (57 >= tc >= 48):
        return [0]
    string += str(tc - 48)
    hashcode = crctable[index[2]] ^ (hashcode >> 8)
    tc = hashcode & 0xff ^ index[1]
    if not (57 >= tc >= 48):
        return [0]
    string += str(tc - 48)
    hashcode = crctable[index[1]] ^ (hashcode >> 8)
    tc = hashcode & 0xff ^ index[0]
    if not (57 >= tc >= 48):
        return [0]
    string += str(tc - 48)
    return [1, string]


def crack(danmu):
    print(f"cracking -> {danmu['midHash']}")
    index = [0 for _ in range(4)]
    i = 0
    ht = int(f"0x{danmu['midHash']}", 16) ^ 0xffffffff
    for i in range(3, -1, -1):
        index[3 - i] = get_crc_index(ht >> (i * 8))
        snum = crctable[index[3 - i]]
        ht ^= snum >> ((3 - i) * 8)
    for i in range(100000000):
        lastindex = crc32_last_index(i)
        if lastindex == index[3]:
            deepCheckData = deep_check(i, index)
            if deepCheckData[0]:
                break
    if i == 100000000:
        return -1
    danmu['mid'] = f"{i}{deepCheckData[1]}"
    crack_list.append(danmu)


# ==================== check-cookies ====================
def check_cookies():
    """
    检测cookies的可用性
    :return: cookies(dict)
    """
    while True:
        try:
            f = open("cookies.txt", "r", encoding="utf-8")
            cookies = f.read()
            cookies = convert_cookies_to_dict(cookies)
            try:
                check_cookie = requests.get("https://api.bilibili.com/x/space/upstat?mid=1", cookies=cookies,
                                            headers=headers).text
            except:
                output_log("E", "无法验证您的cookies.. 请检查您的网络设置，若您开启了代理请先关闭代理。")
                break
            if check_cookie == """{"code":0,"message":"0","ttl":1,"data":{}}""":
                open("cookies.txt", "w+", encoding="utf-8")
                print("校验失败，请检查cookies是否过期并及时更新您的cookies。")
                continue

            return cookies
        except:
            f = open("cookies.txt", "w+", encoding="utf-8")
            cookies = input("cookies> ")
            f.write(cookies)


def convert_cookies_to_dict(cookies):
    """
    将输入的cookies转为可识别的字典类型

    :param cookies: string
    :return: cookies(dict)
    """
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    return cookies


# ==================== Get-Video-Info ====================

def get_info(bvid, cookies):
    """
    获取视频基本信息

    :param bvid: BV号（番剧、视频）
    :param cookies: cookies(dict)

    :return: 视频信息
    """
    data = requests.get(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}",
                        headers=headers,
                        cookies=cookies).text

    data = json.loads(data)["data"]
    video_num = data["videos"]
    title = data["title"]

    pub_time = time.strftime("%Y-%m-%d", time.localtime(data["pubdate"]))

    desc = data["desc"]
    danmuku = data["stat"]["danmaku"]
    name = data["owner"]["name"]
    cid = data["cid"]
    duration = data["duration"]

    dict_info = {"title": title, "pub_time": pub_time, "desc": desc,
                 "danmuku": danmuku, "name": name, "cid": cid, "duration": duration}
    if int(video_num) == 1:
        return dict_info
    else:
        while True:
            try:
                page = int(input("此视频为分P视频，请指定一个page\npage> "))
                dict_info["cid"] = data["pages"][page - 1]["cid"]
                dict_info["title"] = data["pages"][page - 1]["part"]
                dict_info["duration"] = data["pages"][page - 1]["duration"]
                return dict_info
            except:
                continue


def get_ep_key(url):
    """
    获取番剧bvid

    :param url:
    :return: 番剧bvid
    """
    header = {
        "cookie": "_uuid=9D4E10FEF-4CE4-3FD7-CE107-4D1F438110A5229945infoc; buvid3=F94E7751-DA48-4F97-89C9-5A4EE9CF1AA4148817infoc; buvid_fp=F94E7751-DA48-4F97-89C9-5A4EE9CF1AA4148817infoc; video_page_version=v_old_home; blackside_state=1; rpdid=|(J~l|mlYku|0J'uYJ~~u)~)J; CURRENT_BLACKGAP=1; CURRENT_QUALITY=0; CURRENT_FNVAL=80; innersign=0; b_lsid=1FCBBAF8_17E38C696A6; bsource=search_360; PVID=1; buvid_fp_plain=F94E7751-DA48-4F97-89C9-5A4EE9CF1AA4148817infoc; SESSDATA=68181722%2C1657187087%2C2b3ad%2A11; bili_jct=0e3de1c40e32e00990ca7fb365a3350e; DedeUserID=2036429689; DedeUserID__ckMd5=f4d43c2865058f15; sid=ccvhr5mv; i-wanna-go-back=-1; b_ut=5; fingerprint3=a284a6f2bcfcdf907cfb890ae01472e1; fingerprint=bb4d7ec794b31153738097e6b58d32d4; fingerprint_s=03d24d5903476f4db97405b6daaf39c9; bp_video_offset_2036429689=612909923547040740; bp_t_offset_2036429689=612909923547040740",
        "origin": "https://www.bilibili.com",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

    resp = requests.get(url, headers=header)

    # (?P<cid>.*?)
    obj = re.compile(
        r'"bvid":"(?P<bvid>.*?)","cid":(?P<cid>.*?),"cover":"(?P<cover>.*?)",(?P<b>.*?),"link":"(?P<link>.*?)",',
        re.S)
    result = obj.finditer(resp.text)

    for it in result:
        link = it.group("link")
        if url.find(link) != -1:
            bvid = it.group("bvid")
    resp.close()

    return bvid


def get_bvid(url):
    """
    获取一般视频、分P视频的bvid

    :param url: 视频地址
    :return: 视频bvid
    """

    bvid = re.search(r'(BV.*?).{10}', url)
    return bvid.group(0)


# 写废了O.o
# def get_danmu(cookies, cid, date, check=-1):
#     global end, all_danmu, start_date, adds
#     url = f"http://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={cid}&date={date}"
#     resp = requests.get(url, headers=headers, cookies=cookies)
#     output_log("Getting", url)
#     data = resp.content
#
#     danmaku_seg = bili_pb2.DmSegMobileReply()
#     danmaku_seg.ParseFromString(data)
#
#     mode_list = ["普通弹幕", "普通弹幕", "普通弹幕", "普通弹幕", "底部弹幕", "顶部弹幕", "逆向弹幕", "高级弹幕",
#                  "代码弹幕", "BAS弹幕（仅限于特殊弹幕专包）"]
#
#     start_date = date
#
#     dict_danmu = []
#
#     if check == -1:
#         end = time.localtime(danmaku_seg.elems[-1].ctime)
#         end = time.strftime("%Y-%m-%d", end)
#         for j in danmaku_seg.elems:
#             ctime = time.localtime(j.ctime)
#             add = {"midHash": j.midHash, "content": j.content, "ctime": time.strftime("%Y-%m-%d %H:%M:%S", ctime),
#                    "fontsize": j.fontsize, "mode": mode_list[j.mode]}
#             if add not in all_danmu:
#                 dict_danmu.append(add)
#                 all_danmu.append(add)
#
#         output_log("size", len(dict_danmu))
#         if len(dict_danmu) >= 1500:
#             now_time = datetime.strptime(date, "%Y-%m-%d")
#             next_time = (now_time + timedelta(days=+1)).strftime("%Y-%m-%d")
#             get_danmu(cookies, cid, next_time)
#             now_time = datetime.strptime(date, "%Y-%m-%d")
#             next_time = (now_time + timedelta(days=-1)).strftime("%Y-%m-%d")
#             get_danmu(cookies, cid, next_time)
#
#     print(len(all_danmu))
#
#     return dict_danmu

def get_danmu(cid, segment_index, cookies):
    """
    获取全部弹幕并累加到all_danmu

    :param cid: oid
    :param segment_index: 弹幕分包(6min为一包)
    :param cookies: cookies(dict)
    """
    global all_danmu

    url = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_index}'
    resp = requests.get(url, cookies=cookies, headers=headers)
    data = resp.content
    output_log("Getting", url)

    danmaku_seg = bili_pb2.DmSegMobileReply()
    danmaku_seg.ParseFromString(data)

    mode_list = ["普通弹幕", "普通弹幕", "普通弹幕", "普通弹幕", "底部弹幕", "顶部弹幕", "逆向弹幕", "高级弹幕",
                 "代码弹幕", "BAS弹幕（仅限于特殊弹幕专包）"]
    for danmu in danmaku_seg.elems:
        ctime = time.localtime(danmu.ctime)
        add = {"midHash": danmu.midHash, "content": danmu.content, "ctime": time.strftime("%Y-%m-%d %H:%M:%S", ctime),
               "fontsize": danmu.fontsize, "mode": mode_list[danmu.mode], "id": danmu.idStr}
        all_danmu.append(add)


# API有问题，部分日期返回null，废弃
# def get_history_date(cookies, oid, pub_month, pub_year):
#     # https://api.bilibili.com/x/v2/dm/history/index?month=2023-05&type=1&oid=
#     now_month = get_month(time.time()) + 1
#     now_year = get_year(time.time()) + 1
#
#     date_list = []
#     for y in range(pub_year, now_year):
#         if now_year - y > 2:
#             now_month = 13
#         else:
#             if pub_month > now_month:
#                 pub_month = 1
#             now_month = get_month(time.time()) + 1
#
#         for i in range(pub_month, now_month):
#             if i < 10:
#                 str_i = f"0{i}"
#             else:
#                 str_i = f"{i}"
#
#             url = f"https://api.bilibili.com/x/v2/dm/history/index?month={y}-{str_i}&type=1&oid={oid}"
#             data = requests.get(url, headers=headers, cookies=cookies).text
#
#             output_log("Getting", url)
#             print(data)
#
#             try:
#                 for date in json.loads(data)["data"]:
#                     date_list.append(date)
#             except:
#                 pass
#
#     return date_list


# ==================== Tools ====================

def output_log(title, text):
    """
    输出日志

    :param title: 标题
    :param text: 内容
    """
    print(f"[{title}] {text}")


def print_long_line(t=1):
    """
    输出分割线

    :param t: 分割线样式
    """
    if t == 1:
        print("\n==========================\n")
    elif t == 2:
        print("==========================")


def _async_raise(tid, exctype):
    """
    线程杀手，用于提前终止线程

    :param tid: t.ident
    :param exctype: SystemExit
    """
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def StopThread():
    """
    终止所有逆向线程
    """

    global tlist, STOP_FLAG
    for t in tlist:
        STOP_FLAG = True
        try:
            _async_raise(t.ident, SystemExit)
            output_log("STOP", t)
        except:
            pass


def makedirs(folder):
    """
    创建必要文件夹

    :param folder: 文件夹名称
    """
    if not os.path.exists(folder):
        os.makedirs(folder)


def output(msg):
    """
    输出结果并同步输出到文件中

    :param msg: 内容
    """
    global gf
    print(msg)
    gf.write(str(msg) + "\n")


def output_result(danmu):
    """
    输出所有逆向后弹幕信息

    :param danmu: 弹幕
    """
    output("\n==========================")
    output(f"弹幕内容: {danmu['content']}")
    output(f"发送时间: {danmu['ctime']}")
    output(f"字体大小: {danmu['fontsize']}")
    output(f"弹幕类型: {danmu['mode']}")
    output(f"发送者UID: {danmu['mid']}")
    output(f"发送者主页连接: https://space.bilibili.com/{danmu['mid']}")
    output("==========================")


def listToJson(lst):
    """
    将列表转换为json格式，方便其他程序调用

    :param lst: 列表
    :return: json(string)
    """
    str_json = json.dumps(lst, indent=2, ensure_ascii=False)
    return str_json


# ==================================================


def main():
    """
    主函数
    """

    global crack_list, tlist, STOP_FLAG, gf, all_danmu

    cookies = check_cookies()
    while True:
        url = input("bvid&url> ")
        try:
            bvid = get_bvid(url)
            output_log("BVID", bvid)
            break
        except:
            if input("[?] 无法匹配到该视频，你是否需要匹配番剧？(n/*)") == "n":
                continue

            try:
                bvid = get_ep_key(url)
                break
            except:
                output_log("E", "无法找到此番剧。")
                continue

    output_log("/", "获取视频/番剧基本信息...")
    data = get_info(bvid, cookies)
    cid = data["cid"]
    title = data["title"]
    danmuku = data["danmuku"]
    desc = data["desc"]
    pub_time = data["pub_time"]
    duration = data["duration"]

    print_long_line(2)
    output_log("CID", cid)
    output_log("标题", title)
    output_log("弹幕库(?)", danmuku)
    output_log("描述", desc)
    output_log("视频时长", f"{duration}s")
    output_log("发布时间", pub_time)
    print_long_line(2)

    if input("信息无误？(n/*)") == "n":
        main()

    output_log("/", "正在获取全部弹幕...")

    start_time = time.time()
    for i in range(math.ceil(duration / (60 * 6))):
        get_danmu(cid, i + 1, cookies)

    end_time = time.time()

    print(f"弹幕获取完成，耗时{round(end_time - start_time, 2)}秒")

    if len(all_danmu) == 0:
        output_log("E", "此视频没有任何弹幕，请解析其它视频。")
        main()
    output_log("danmu_size", len(all_danmu))

    f = open(f"DanmuJSON/danmu_list_{bvid}.json", "w", encoding="utf-8")
    f.write(listToJson(all_danmu))
    f.close()

    print(
        "\n\n全部弹幕信息已构造完成，请输入关键字(你想要搜索的弹幕内容)来检索弹幕。 若要搜索全部弹幕，请先回车后再输入all来搜索")
    while True:
        STOP_FLAG = False
        crack_list = []
        ftext = input("搜索弹幕> ")
        if ftext == "":
            print("你没有输入任何关键词，请输入关键词后检索！\n若需要检索全部弹幕，请输入'all'")
            if input() != "all":
                continue

        flist = []
        gf = open(f"outputs/{ftext}_{bvid}.txt", "a+", encoding="utf-8")

        for danmu in all_danmu:
            content = danmu["content"]
            if content.find(ftext) != -1:
                flist.append(danmu)
                print(f"检索到弹幕 -> {content} ...")

        if input("按下回车进行midHash逆向操作(UID反推)。这可能需要一点时间.. 'n'取消") == "n":
            continue
        start_time = time.time()
        tlist = []
        for danmu in flist:
            if STOP_FLAG:
                break
            create_table()
            t = Thread(target=crack, args=(danmu,))
            t.start()
            tlist.append(t)

        for t in tlist:
            t.join()

        end_time = time.time()

        for danmu in crack_list:
            output_result(danmu)

        print(f"所有UID反推成功，耗时{round(end_time - start_time, 2)}秒")
        gf.close()
        if input("回车继续检索，输入q退出...") == "q":
            break

        print_long_line()


if __name__ == '__main__':
    keyboard.add_hotkey('`', StopThread)
    print_long_line(2)
    print("GetDanmuSender 1.0b - By cwuom\nbilibili> https://space.bilibili.com/473400804")
    print_long_line(2)

    makedirs("DanmuJSON")
    makedirs("outputs")
    main()
