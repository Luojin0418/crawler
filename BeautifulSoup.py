import os
import requests
from bs4 import BeautifulSoup

def getPage(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'#不设置的话，中文会出现乱码
        return response.text
    print('wrong connection')
    return None

url = 'https://maoyan.com/board'
html = getPage(url)
soup = BeautifulSoup(html, 'lxml')

title = soup.find_all(class_='name')#爬取电影的标题
author = soup.find_all(class_='star')#爬取主演
releasetime = soup.find_all(class_='releasetime')#爬取上映时间
image = soup.find_all('img',class_='board-img')#爬取图片

#爬取评分
integer = soup.find_all(class_='integer')#整数部分
fraction = soup.find_all(class_='fraction')#小数部分


#写入文件
with open('Result.txt', 'a', encoding='utf-8') as f:
    for i in range(len(title)):
        f.write(title[i].string.strip()+'('+integer[i].string.strip()+fraction[i].string.strip()+')'+'\n'+author[i].string.strip()+'\n'+releasetime[i].string.strip())
        f.write('\n')

if (not os.path.exists('image')):
    os.mkdir('image')

for i in image:
    name = i['alt']
    picturelink = i['data-src']
    Paths = 'image/'+name+'.png'
    with open (Paths, 'wb') as f:
        r = requests.get(picturelink)
        f.write(r.content)
