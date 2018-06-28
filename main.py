from PIL import ImageGrab
from PIL import Image
import math
import operator
from functools import reduce

def likeCoefficient(pic1,pic2):
    image1 = Image.open(pic1)
    image3 = Image.open(pic2)
    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image3.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result
def screen():
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    bbox = (0, 0, 1920, 1080)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    im.save('as.png')
def compare():
    return


#开始游戏
#返回大厅
#确认
#Esc
#重启大厅