import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
import urllib.parse
url='https://www.starbucks.com.cn/menu/'
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22188b52627181cf-061f2efc6b090f8-7e56547b-2073600-188b5262719cab%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4YjUyNjI3MTgxY2YtMDYxZjJlZmM2YjA5MGY4LTdlNTY1NDdiLTIwNzM2MDAtMTg4YjUyNjI3MTljYWIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188b52627181cf-061f2efc6b090f8-7e56547b-2073600-188b5262719cab%22%7D; ZHh6ku4z=AzU2JrWIAQAAgd_o3LZzlfTWN3GA90Xv1g8I4B3aU-6qpXUmt-F7XfZggR-UAXkjtwAXThRAwH8AAEB3AAAAAA|1|1|b9bf1b15c7cb1696913d7babb3b3bf8ed09bab30',
'Host':'www.starbucks.com.cn',
'Referer':'https//www.starbucks.com.cn/',
'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)

from bs4 import BeautifulSoup
soup=BeautifulSoup(content,'lxml')
name_obj=soup.select('ul>li>a>strong')
pic_obj=soup.select('ul>li>a>div')

for i in range(len(name_obj)):
    name = name_obj[i]
    name_list = name.getText()
    print(name_list)
    pic=pic_obj[i]
    pic_list=pic.attrs.get('style')
    startindex=pic_list.index("(")
    endindex=pic_list.index((")"))
    pic_list=pic_list[startindex+2:endindex-1]
    pic_list="http:/"+pic_list
    print(pic_list)




# pic_obj=soup.select('ul>li>a>div')[0]

# name_list=name_obj.getText()
# pic_list=name_obj.attrs.get('style')



