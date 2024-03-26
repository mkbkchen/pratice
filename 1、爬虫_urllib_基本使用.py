#使用urllib获取百度首页的源码
import urllib.request

#（1）定义一个url，就是要访问的地址
url='http://www.baidu.com'

#（2）模拟浏览器向服务器发送请求 response响应
response=urllib.request.urlopen(url)

#（3）获取响应中的页面的源码 content 内容
#read返回的字节形式的二进制数据
#我们要将二进制的数据转换成字符串
#二进制-->解码 decode（'编码的格式'）
content=response.read().decode('utf-8')

#（4）
print(content)