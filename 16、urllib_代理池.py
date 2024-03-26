proxies_pool=[
    {'http':'118.24.219.151:168171111'},
    {'http':'118.24.219.151:16817222'},
]

#利用随机性来实现
import random
proxies=random.choice(proxies_pool)
print(proxies)

import urllib.request
url='https://www.baidu.com/s?wd=ip'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
request=urllib.request.Request(url=url,headers=headers)

handler=urllib.request.ProxyHandler(proxies=proxies)

opener=urllib.request.build_opener(handler)

response=opener.open(request)

content=response.read().decode('utf-8')
#保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)