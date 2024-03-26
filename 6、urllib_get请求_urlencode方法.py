#urlencode应用场景：多个参数的时候
# https://www.baidu.com/s?wd=周杰伦&sex=男
# import urllib.parse
# data={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
# a=urllib.parse.urlencode(data)
# print(a)

#1、获取网页源码
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81
import urllib.request
import urllib.parse

base_url='https://www.baidu.com/s?'
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
#获取data的unicode码
newdata=urllib.parse.urlencode(data)
#得到网页源码——请求资源路径
url=base_url+newdata
print(url)

#2、获取内容
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')
print(content)
                                                                                                                                                                                                                                            