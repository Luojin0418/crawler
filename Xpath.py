
import requests
import re
from lxml import etree
import time

def getPage(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'gbk'#不设置的话，中文会出现乱码
        return response.text
    print('wrong connection')
    return None


def write_to_file(content):
    with open('spider.txt', 'a', encoding='utf-8') as f:
        f.write(content+'\n')

def write_to_href(href):
    with open('href.txt', 'a', encoding='utf-8') as f:
        f.write(href+'\n')

# 读取首页并爬取所有的链接
url0 = "https://www.wenku8.net/novel/1/1973/"
html0 = etree.HTML(getPage(url0))

href = html0.xpath('//td/a/@href')

for i in href:
    i = i+''
    write_to_href(i)

with open('href.txt', 'r') as f:
    while(1):
        str = f.readline()
        if (not str):
            break
        # 爬取某一页上的内容
        url = "https://www.wenku8.net/novel/1/1973/"+str
        # time.sleep(1)
        html = etree.HTML(getPage(url))

        #会把每一次取出来的东西放在List里面
        title = html.xpath('//div[@id="title"]/text()')
        context = html.xpath('//div[@id="content"]/text()')


        write_to_file(title[0]) # 因为title只有一个，而xpath提取出来会放在数组里，所以只用写第一个

        for a in context:
            a = a+''#change to String
            write_to_file(a.strip()) #去除字符串前后中的一些非打印字符
