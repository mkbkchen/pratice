#适用于每次登录cookie都不一样
#动态cookie和代理不能使用请求对象的定制

#需求：适用handler访问百度，获取网页源码
import urllib.request

url='http://www.baidu.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
#请求头的定制
request=urllib.request.Request(url=url,headers=headers)
#handler  build_opener  open
#(1)获取handler对象
handler=urllib.request.HTTPHandler()

#（2）获取opener对象
opener=urllib.request.build_opener(handler)

#(3)调用open方法
response=opener.open(request)

content=response.read().decode('utf-8')
print(content)