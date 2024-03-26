import urllib.request
import urllib.error
# url='https://blog.csdn.net/sulixu/article/details/1198189491'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
#HTTPError
#urlerror：主机地址和参数有问题
url='http://www.douban1111.com'
try:
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级。。。')
except urllib.error.URLError:
    print('我都说了，系统正在升级。。。')