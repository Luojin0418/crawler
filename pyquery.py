# 不能命名为pyquery.py, 否者无法运行, 会和库里的pyquery重复, 导致提示import失败

import os
from pyquery import PyQuery as py

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

def savefile(path, title, content):
    with open(path+title+'.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def saveurl(content):
    with open('all-url.txt','a',encoding='utf-8') as f:
        f.write(content+'\n')

# '\'是转义字符
def filename_deal(fname):
    noexcep = ['\\' , '/' , ':' , '?' , '\"' , '<' , '>' , '|' ]#文件名不能包含这些字符
    for i in noexcep:
        fname=fname.replace(i,'')
    return fname

doc = py('https://news.sina.com.cn/',headers=headers, encoding='utf-8')
mainnews = doc('#blk_yw_01 [href]')

for i in mainnews.items():
    name = i.text()
    url = i.attr('href')
    if 'http' in url:
        saveurl(name+'>'+url)

if (not os.path.exists('news')):
    os.mkdir('news')

with open('all-url.txt', 'r', encoding='utf-8') as f:
    while(1):
        line = f.readline()
        if (not line):
            break
        var = line.split('>')
        name = filename_deal(var[0])
        url = var[1]
        newspage = py(url.strip(), headers=headers, encoding='utf-8')
        content = newspage('#article p').text()
        savefile('news/',name, content)