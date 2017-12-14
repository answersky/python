import urllib.request
import sys
from bs4 import BeautifulSoup
import http.cookiejar

print(sys.getdefaultencoding())

response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode('utf-8', 'ignore')

doc = BeautifulSoup(html, "html.parser")
title = doc.find('title').get_text()
print(title)

# 模拟登陆

url="https://oms.qegoo.cn/user/go_login"
# request = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
# print(request)
values = {"username":"2048875230qq.com","password":"123456"}
# 根据抓包信息 构造表单
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
cj = http.cookiejar.CookieJar()
httphandler = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(httphandler)
response=opener.urlopen(req)
result = response.read().decode('utf-8', 'ignore')
print(result)