# -*- coding: utf-8 -*-
from PIL import ImageGrab
from PIL import Image
import math
import time
import operator
from functools import reduce

import press

home = "img/home.png"
returnBack = "img/returnBack.png"
confirm = "img/confirm.png"
cancel = "img/cancel.png"
returnPoint = {770, 350, 1150, 700}
confirmPoint = {0, 354, 1920, 726}

def likeCoefficient(pic1, pic2):
    image1 = Image.open(pic1)
    image3 = Image.open(pic2)
    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image3.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result


def screen(lu, ru, ld, rd):
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    bbox = (lu, ru, ld, rd)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    im.save('as2.png')


time.sleep(10)
screen(0, 354, 1920, 726)
press.getCurPos()
# 开始游戏
# 返回大厅
# 确认
# Esc
# 重启大厅

# i = 0
# while i < 10:
#     time.sleep(5)
#     print("开始")
#     press.start()
#     time.sleep(20)
#     print("退出")
#     press.cancel()
#     time.sleep(10)
