# -*- coding: utf-8 -*-
from aip import AipOcr
import os
import json
def load():
    with open("properties.json", 'r') as f:
        result = json.load(f)
        APP_ID = result["baidu"]["APP_ID"]
        API_KEY = result["baidu"]["API_KEY"]
        SECRET_KEY = result["baidu"]["SECRET_KEY"]
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        return client
# print(APP_ID)
# print(API_KEY)
# print(SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def getString(pic):
    result = ""
    image = get_file_content(pic)
    ocrResult = load().basicGeneral(image)
    num = ocrResult["words_result_num"]
    i=0
    while i<num :
        result += ocrResult["words_result"][i]["words"]
        i+=1
    print(result)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return result
    # result = ocrResult["words_result"][0]["words"]
    # print result
    # return result


# getString("img/confirm.png")
# getString("img/cancel.png")
# getString("img/returnBack.png")
# getString("img/start.png")
#
# """ 读取图片 """

#
# image = get_file_content('example.jpg')
#
# """ 调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)
#
# url = "https//www.x.com/sample.jpg"
#
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)
