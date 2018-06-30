# -*- coding: utf-8 -*-
import httplib
import md5
import urllib
import urllib2
import random
import json
import base64

httpClient = None

def ocr(pic):
    with open("properties.json", 'r') as f:
        result = json.load(f)
        appKey = result["youdao"]["appKey"]
        secretKey = result["youdao"]["secretKey"]
    try:
        f = open(pic, 'rb')  # 二进制方式打开图文件
        img = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()

        detectType = '10012'
        imageType = '1'
        langType = 'en'
        salt = random.randint(1, 65536)

        sign = appKey + img + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        data = {'appKey': appKey, 'img': img, 'detectType': detectType, 'imageType': imageType, 'langType': langType,
                'salt': str(salt), 'sign': sign}
        data = urllib.urlencode(data)
        req = urllib2.Request('http://openapi.youdao.com/ocrapi', data)

        # response是HTTPResponse对象
        response = urllib2.urlopen(req)
        print response.read()
        print response.read()["Result"]["regions"]
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
# ocr("return.png")
def parse(str):
    result = ""
    arr1 = str["Result"]["regions"]
    for i in arr1 :
        arr2 = arr1[i]["lines"]
        print(arr2)
        # for j in arr2 :
        #     result += arr2[j]["text"]

    print(result)

str = {"errorCode":"0","Result":{"orientation":"UP","regions":[{"boundingBox":"115,24,267,24,267,58,115,58","lines":[{"boundingBox":"115,24,267,24,267,58,115,58","words":[{"boundingBox":"123,24,149,23,149,58,123,59","word":"系"},{"boundingBox":"157,23,191,23,191,58,157,58","word":"统"},{"boundingBox":"200,23,234,23,234,58,200,58","word":"菜"},{"boundingBox":"242,23,267,23,267,58,242,58","word":"单"}],"text":"系统菜单","lang":"zh"}]},{"boundingBox":"162,107,215,107,215,130,162,130","lines":[{"boundingBox":"162,107,215,107,215,130,162,130","words":[{"boundingBox":"168,107,192,107,192,131,168,131","word":"返"},{"boundingBox":"198,107,215,107,215,131,198,131","word":"回"}],"text":"返回","lang":"zh"}]},{"boundingBox":"163,174,215,174,215,197,163,197","lines":[{"boundingBox":"163,174,215,174,215,197,163,197","words":[{"boundingBox":"168,174,192,174,192,198,168,198","word":"设"},{"boundingBox":"198,174,215,174,215,198,198,198","word":"置"}],"text":"设置","lang":"zh"}]},{"boundingBox":"123,241,258,241,258,264,123,264","lines":[{"boundingBox":"123,241,258,241,258,264,123,264","words":[{"boundingBox":"128,240,152,240,152,264,128,264","word":"返"},{"boundingBox":"158,240,176,240,176,264,158,264","word":"回"},{"boundingBox":"182,240,205,240,205,264,182,264","word":"至"},{"boundingBox":"211,240,229,240,229,264,211,264","word":"大"},{"boundingBox":"235,240,258,241,258,265,235,264","word":"厅"}],"text":"返回至大厅","lang":"zh"}]},{"boundingBox":"135,308,243,308,243,330,135,330","lines":[{"boundingBox":"135,308,243,308,243,330,135,330","words":[{"boundingBox":"140,307,163,307,163,331,140,331","word":"退"},{"boundingBox":"169,307,186,307,186,331,169,331","word":"出"},{"boundingBox":"192,307,215,308,215,332,192,331","word":"游"},{"boundingBox":"221,308,243,307,243,331,221,332","word":"戏"}],"text":"退出游戏","lang":"zh"}]}]}}
parse(str)

