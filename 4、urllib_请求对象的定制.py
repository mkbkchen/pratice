import urllib.request

url="https://www.baidu.com"
#url组成
#https://www.baidu.com/s?wd=周杰伦
#http/https www.baidu.com   80/443    s     wd=周杰伦     #
#协议        主机            端口号     路径   参数         锚点
# http    80
# https   443
# mysql   3306
# oracle  1521
# redis   6379
# mongodb 270107

#1、UA反爬
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}
#因为urlopen方法中不能存储字典，所以headers不能传入
#请求对象的定制
#因为参数顺序问题，不能直接写url和headers，中间还有个data,需要关键字传参
request=urllib.request.Request(url=url, headers=headers)

response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)