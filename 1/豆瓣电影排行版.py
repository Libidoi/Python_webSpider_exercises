# get请求 获取豆瓣第一页数据 并且保存

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}

# 1、请求头对象的定制
request = urllib.request.Request(url=url, headers=headers, )
# 2、获取相应数据
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
print(context)

# 3、将数据下载本地
#open方法默认是用gbk编码 如果需要保存，则改成
#encoding = 'utf-8'
fp = open('douban.json', 'w', encoding='utf-8')
fp.write(context)
#方式二：
# with open('douban.json', 'w', encoding='utf-8')
#     fp.write(context)