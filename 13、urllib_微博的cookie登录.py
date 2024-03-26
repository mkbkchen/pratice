#适用的场景：数据采集的时候，需要绕过登录，然后进入到某个页面
#个人信息页面是utf-8,还报错了编码错误，因为没有进入个人信息页面，而是进入了登录页面，登录页面不是utf-8，gb312
#什么情况访问不成功
#因为请求头的信息不够，所以访问不成功


import urllib.request
url='https://weibo.cn/19129315365/info'

headers={
# ':authority':' m.weibo.cn',
# ':method':' GET',
# ':path':' /19129315365/info',
# ':scheme':' https',
'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 'accept-encoding':' gzip, deflate, br',
'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'cache-control':' max-age=0',
    #cookie中携带者登录信息，如果有了登录之后的cookie，我们就可以携带者进入登录后的任何页面
    #referer 一般做图片的防盗链
'cookie':' __bid_n=188681f4917a63687f4207; FPTOKEN=EqtQoT9VCFeUUSeXFq57s5GfiVjwIXCMhAKswvWZ6ScfJLF2TIQ2LJf29NegOhtfLc36Cw7Ry2DrhIyieGSAAgKbnwad1BQh9gp5T2dRyqF4fH7Yt4m8/xBM52F1aAOZdI7R7qM4qnxh6uMVGfdk+RCkEsn37qcJHgvLW2qOV7pHJMSCuEBsB1SfVi9Y1vAXGwmnGrFubEwZTilKluJnaM4z4A9G+KZbsBx9fhlg8StpWGlYMMQGfqmfN2X3nF/XZuQREVKXG44tzis0oCCgtEqIx7zdBex2x9y1++T2HcbOLH30Tnb1mTp7ExhHBXRJhQyAEPpB/7rpqh++hASR+hbveVQd+91G7S4IQ/AOmuRe2Q7TUgchkOAMO4sLnEA1645HFZABnO+zSohTyMI0Ug==|1oyDPe4zGUJFaXc+DmGfeig5eCVU4K/7VstsZMeczRY=|10|506cec0c5a4b383ca5bdd7411b429c56; _T_WM=a6da57d9127869f3db1e785038843465; SUB=_2A25JcmkfDeRhGeNJ41QX9izEyzmIHXVqnXdXrDV6PUNbktANLU3skW1NS40chFjICAqxb8m1WZNXUPmyF9deo-RJ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5aJBH-RKCILCQOTCknr_ca5JpX5KzhUgL.Fo-N1hqcSozReh-2dJLoIEBLxKqLBoMLB--LxKqL1--LBoeLxKnLBoBL1-BLxKnLBoBL1-Bt; SSOLoginState=1685461327; ALF=1688053327; XSRF-TOKEN=c197cb; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174; mweibo_short_token=ccd6dbbffe',
'sec-ch-ua':' "Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
'sec-ch-ua-mobile':' ?0',
'sec-ch-ua-platform':' "Windows"',
'sec-fetch-dest':' empty',
'sec-fetch-mode':' navigate',
'sec-fetch-site':' same-origin',
'upgrade-insecure-requests':' 1',
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
}
#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
#获取响应的数据
content=response.read().decode('utf-8')

#将数据保存到本地
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)  #进入的是登录页面