#第一页
# url='https://sc.chinaz.com/tupian/qinglvtupian.html'
#第三页
# url='https://sc.chinaz.com/tupian/qinglvtupian_3.html'
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import urllib.parse
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

start_page = int(input('请输入起始页码'))
end_page = int(input('请输入结束页码'))
for page in range(start_page, end_page + 1):
    if page==1:
        url='https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)

    tree = etree.HTML(content)
        #一般涉及到图片的网站都会设计懒加载
    src_list = tree.xpath('//div[@class="container"]//div/img/@data-original')
    name_list=tree.xpath('//div[@class="container"]//div/img/@alt')
        # for src,name in src_list,name_list:
        #下载图片



    for i in range(len(name_list)):
        src1=src_list[i]
        name1=name_list[i]
        src='https:'+src1
        name=name1+'.jpg'
        urllib.request.urlretrieve(src, filename="F://zmy//图片//"+name)






