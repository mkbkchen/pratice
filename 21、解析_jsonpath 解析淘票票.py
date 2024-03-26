import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request


url='https://dianying.taobao.com/cityAction.json?city=110100&_ksTS=1686480806771_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'
headers={
# ':Authority':'dianying.taobao.com', #前面带冒号的都不能用
# ':Method':'GET',
# ':Path':'/cityAction.json?city=110100&_ksTS=1686480806771_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
# ':Scheme':'https',
'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# 'Accept-Encoding':'gzip, deflate, br', 这个需要注释掉
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cookie':'cna=Hne1F2V7uUECAXAKQBE6czpT; tracknick=%5Cu840C%5Cu9762%5Cu8D85%5Cu4EBA741; enc=r887%2FObU3sa4VdtVt6olI1%2Fd4GLPBHAznVkFG9yG9AeIa7zJCvlVaOntlihsYm3MnPqJ7T6m1iZUbFxtn%2B0rtQ%3D%3D; miid=814744754636759992; thw=cn; sgcookie=E1006OYjJZ1u46hOSMKKNPU48eHgttkmIe1s9SuXjpybqLeffzjicaLk3B7x0zoqnIXS87EvEUQNK9tzaAtHGLUqY6PzkJ0BOgJAzMgx3zzolQMQdVgCeNqQ%2FU3EqOwmEAaA; _cc_=UtASsssmfA%3D%3D; t=2e2c93f723f577a495f7355d330f4a63; cookie2=15f0802b284cc36544b1b5b83e16491e; v=0; _tb_token_=fe81d5e90b570; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; isg=BGxsvpJSJLplHzB0E9QPKNgiPUqeJRDPSPo1_sar15e70Qfb7jRpXhYo8Znp3Ugn; l=fBSygScrNwvqnZ8iBO5Bhurza77OVBRX1oVzaNbMiIEGa6TN1FsuVNC1NmoMRdtjgT52UetrqYnVTdUy8xz38jkDBeYQKtyuJTv68eM3N7AN.; tfstk=cxmPBetso3KP-PDp6oqE_ADPpzyRaMHoKiy_rIbQtEMvvK2Y_sVd9-VQd-yC364l.',
'Referer':'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.45bb112aRWpWbN&city=110100', #这个要注意
'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'Windows',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41',
'X-Requested-With':'XMLHttpRequest'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
#去掉左圆括号之前，和后圆括号之后的不要
content=content.split('(')[1]
print(content)
content=content.split(')')[0]
print(content)

with open('21、解析_jsonpath 解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
#排版json文件 ：ctrl+alt+l

import json
import jsonpath

#读取json文件
obj=json.load(open('21、解析_jsonpath 解析淘票票.json', 'r', encoding='utf-8'))  #文件
# 解析json文件，只能读文件，因此上面必须是文件
name_list=jsonpath.jsonpath(obj,'$..name')
print(name_list)