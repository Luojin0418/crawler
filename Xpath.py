'''
只能根据网页上的排版来写入文件，无法自定义格式。
'''


import requests
import re
from lxml import etree

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
        f.write(content + '\n')



url = "https://www.wenku8.net/novel/1/1973/69567.htm"
html = etree.HTML(getPage(url))

#会把每一次取出来的东西放在List里面
title = html.xpath('//div[@id="title"]/text()')
context = html.xpath('//div[@id="content"]/text()')
#context = context.replaceAll('\r\n\xa0\xa0\xa0\xa0','')
# print(title)
# print(context[4])
write_to_file(title[0])
print(context)
for a in context:
    a = a+''#change to String
    write_to_file(a)