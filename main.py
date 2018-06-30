# -*- coding: utf-8 -*-
import time
import baiduOcr
import screen
import press
temp = "as.png"
def read():
    time.sleep(5)
    screen.screen(0, 0, 1920, 1080, temp)
    return baiduOcr.getString(temp)
def run():
    time.sleep(10)
    i = 0
    while i<1000 :
        judge(read())
        i+=1
def judge(str):
    if(str.__contains__("选择战场")|str.__contains__("开始")|str.__contains__("队伍")):
        start()
        time.sleep(60)
        esc()
        return "start"
    elif(str.__contains__("系统菜单")|str.__contains__("返回至大厅")|str.__contains__("设置")):
        returnBack()
        return "returnBack"
    elif (str.__contains__("确定要") |str.__contains__("放弃吃鸡") |str.__contains__("确定")):
        confirm()
        return "confirm"
    elif (str.__contains__("RECONNECT MATCH") |str.__contains__("比赛仍在进行中") |str.__contains__("继续")):
        cancel()
        return "cancel"
    elif (str.__contains__("重新连接") |str.__contains__("reconnect")|str.__contains__("服务器繁忙") ):
        reConnect()
        return "reConnect"
    elif (str.__contains__("error") |str.__contains__("busy") |str.__contains__("选择战场")):
        esc()
        return "error"
    else:
        esc()
        return "Unkonw Error"
def start():
    if(press.start()!=1):
        start()
    else:
        return

def esc():
    if (press.esc() != 1):
        esc()
    else:
        return
def returnBack():
    if (press.returnBack() != 1):
        returnBack()
    else:
        return

def confirm():
    if (press.confirm() != 1):
        confirm()
    else:
        return

def cancel():
    if (press.cancel() != 1):
        cancel()
    else:
        return
def reConnect():
    if (press.reConnect() != 1):
        cancel()
    else:
        return


run()
