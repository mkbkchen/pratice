#X-Requested-With: XMLHttpRequest 就是ajax
#第一页
#http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

#表单数据
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10
#第二页
#http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#表单数据
#cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

def get_content(page):
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
    data={
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
        'pageSize': 10
    }
    data=urllib.parse.urlencode(data).encode('utf-8')
    request=urllib.request.Request(url=url,data=data,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return  content

if __name__=='__main__':
    start_page=int(input('请输入起始页码'))
    end_page=int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        content=get_content(page)
        fp=open('kfc'+str(page)+'.json','w')
        fp.write(content)
