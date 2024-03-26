import urllib.request
url='https://www.jd.com/'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
print(content)
#网址的：shortcut-2014，在content中找不到