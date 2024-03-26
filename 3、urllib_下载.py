import ssl
ssl._create_default_https_context = ssl._create_unverified_context


import urllib.request

#下载网页
url_page='http://www.baidu.com/'
#url代表下载路劲，filname代表文件的路径
#在python中可以写变量的名字，也可以直接写值
urllib.request.urlretrieve(url_page,'baidu.html')

#下载图片
url_img="https://bkimg.cdn.bcebos.com/pic/3bf33a87e950352ac65c09207e0aecf2b21193131dc8?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxNTA=,g_7,xp_5,yp_5"
urllib.request.urlretrieve(url_img,filename="lisa.jpg")

#下载视频
url_video="https://haokan.baidu.com/03065205-97c4-4df1-8335-334cec039f96"
urllib.request.urlretrieve(url_video,"lisa.mp4")
