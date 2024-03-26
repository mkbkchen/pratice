
#post请求
#找接口
   #network——all——sug——form data下面为'kw':'spider'

import urllib.request
import urllib

url='https://fanyi.baidu.com/sug'  #请求路径

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64010 ; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}  #请求头

data={
    'kw':'spider'} #请求参数

#post请求的参数必须进行编码
data=urllib.parse.urlencode(data).encode('utf-8')

#post请求参数是不会拼接在url后面的，而是需要放在请求对象定制的参数中
#post请求的参数必须进行编码
#请求对象的定制
request=urllib.request.Request(url=url,data=data,headers=headers)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

#读取请求的内容
content=response.read().decode('utf-8')

print(content)  #字符串

#字符串变成json对象
import json
obj=json.loads(content)
print(obj)

#post请求方式的参数必须进行编码 data=urllib.parse.urlencode(data)
#编码之后必须调用encode方法    data=urllib.parse.urlencode(data).encode('utf-8')
#参数放在请求对象定制的方法中    request=urllib.request.Request(url=url,data=data,headers=headers)