#post请求

import urllib.request
import urllib.parse
url='https://fanyi.baidu.com/translate?aldtype=16047&'
#内容是请求标头的数据，用editplus
#只需要cookie
headers={
'Cookie': 'SOUND_PREFER_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; BIDUPSID=F2EB9ED31FA527E7FDE10D3ACEB05FFF; PSTM=1592792557; MCITY=179-179%3A; BAIDUID=C2C320FE22D3B9FE689BD175F323F876:FG=1; BDUSS=Fk4R2V-ZW9nNUZmRFhRaXMzUGdsR28wQWVmTVhkOXNsM1lNeEREM2FFM21rR2xrSVFBQUFBJCQAAAAAAQAAAAEAAAAzR1RMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOYDQmTmA0JkS; BDUSS_BFESS=Fk4R2V-ZW9nNUZmRFhRaXMzUGdsR28wQWVmTVhkOXNsM1lNeEREM2FFM21rR2xrSVFBQUFBJCQAAAAAAQAAAAEAAAAzR1RMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOYDQmTmA0JkS; BAIDUID_BFESS=C2C320FE22D3B9FE689BD175F323F876:FG=1; ZFY=ZtWJEgB11GLSoRx2wYhD0mS2h08SiODwBtFC7esY03c:C; APPGUIDE_10_0_2=1; __bid_n=1861ade9b91f3d62594207; FPTOKEN=8CK/c+VsQ7kFTOdsAOPwJn9VdsQoQAeEQzCORliaswbg5djN4rg6jnJVFQhDdAWnfdInaT1kPPVKNDH3cdkoeBGpekVngEChFNQpoiztL+oU9IcBpEXcFV9OpRnaKA/zhuMJnEN9Xgp5QftMvYmPHU6/Wc2MVpF4jtfc+VL8K8g+y8oKKfhSCccLCfZH4yYpP7lixq1LyjwDny/LvcbTENFRWYRB7wSIxkIVFX/MbazQYwytHub+q/eOBTqzwM4rIy4CMJyQ1y7zDGTiDOG8omsioKsN1WJZH+c+HpdrewFJ2JJ3ZGPpRaDR/meh1TYwdVP5vIpjIz8FT817/C8Hcdi09WEAheUqRUj3El41+GnJikhjGLelym6lwyCKT3X2J0WUqlwhdpKzYo5YtHZOXA==|/pn6FsDatVzkHwUfE/2sG03fGsVwczRo+3coDGo8aLw=|10|50b3616a72333584d4559c35e6658c8c; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1683040614,1683294773,1685023833; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1685024712; ab_sr=1.0.1_ZGVlMjMzOTI4MjJlMDI0NmI1MTMxOTYxYzg2YjE5OGEwYTA3MmZhNWYwZGI2ZWU3YTc0ZWRmZTg3Zjg0OWU0MDE4ZWM3Mzk2NjliYjZhMmQ5YWFjMzhlMTc1ODhhZTllMTUzNjNjNTNlNWVkYmYxZTU1MTc3ZjBiOGNlMzc3NDZjNzUwMzI2ZWU3NGU2NjFlMTNjNDQ3OGM4YzQyZGI2NDJjYjVkMmU4YzdkMmQyN2YzMWU5YjI0Yzk0NzkzMWE2'
}
# 取自 network——v2transapi..——form data
data={
'from':'en',
'to':'zh',
'query': 'love',
'simple_means_flag': '3',
'sign': '198772.518981',
'token': '2853b603854d648a09e1b46a7decea0e',
'domain': 'common',
'ts': '1685024712582'
}
#post请求的参数，必须进行编码，并且调用encode方法
data=urllib.parse.urlencode(data).encode('utf-8')
#请求对象的定制
request=urllib.request.Request(url=url,data=data,headers=headers)
#模拟浏览器像服务器发送请求
response=urllib.request.urlopen(request)
#获取响应的内容
content=response.read().decode('utf-8')
print(content)


#字符串变成json对象
import json
obj=json.loads(content)
print(obj)