#get请求
#获取豆瓣电影第一页的数据，并且保存起来
#网络——全部——预览——toplist？type。。
import urllib.request
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}
#(1)请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#(2)模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
#(3)读取内容
content=response.read().decode('utf-8')
print(content)
#（4）数据下载到本地
#open方法默认使用gbk的编码，如果我们想保存汉字，u啊泡澡open方法中制定编码格式utf-8
fp=open('douban.json','w',encoding='utf-8')
fp.write(content)
