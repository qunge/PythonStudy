from urllib import request
from bs4 import BeautifulSoup
import os
import uuid


# url = 'http://bbs.voc.com.cn/viewthread.php?tid=5549653'

# 保存图片
def getImg(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    req = request.Request(url, headers=headers)
    resp = request.urlopen(req).read()
    soup = BeautifulSoup(resp, 'html5lib')
    # 创建文件夹
    path = r'D:\img\{0}'.format(soup.select('div.spaceborder')[1].find('a').text.replace(' ',''))
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    existPath = os.path.exists(path)
    # 如果不存在创建路径
    if not existPath:
        os.makedirs(path)
    items = soup.findAll('img', alt='按此在新窗口浏览图片')
    # 保存图片
    for item in items:
        src = item.get('src')
        print(src)
        request.urlretrieve(src, path + '\%s.jpg' % (uuid.uuid4()))

    getNextUrl(soup)

# 获取下一页URl
def getNextUrl(soup):
    if soup:
        tag = soup.find('a', text='下一页»')
        if tag:
            urltail = tag.get('href')
            if urltail:
                getImg('http://bbs.voc.com.cn/' + urltail)


try:
    url = input('请输入网址：')
    getImg(url)
except Exception as asaa:
    print(asaa)