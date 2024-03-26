#网络——全部——预览——toplist？type。。
#第一页
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20
import urllib.request
import urllib.parse


#第二页
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

#page  1  2  3  4
#start 0  20  40  60
# start=(page-1)*20

#下载豆瓣电影前十页的数据
#（1)请求对象的定制

#（2）获取响应的数据

#(3)下载数据

def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data={'start':(page-1)*20,
          'limit':20
    }
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    newdata=urllib.parse.urlencode(data)
    url=base_url+newdata
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)


    start_page=int(input('请输入起始页码'))
    end_page=int(input('请输入结束页码')) #左闭右开
    for page in range(start_page,end_page+1):
        # 每一页都有自己请求对象的定制
        request=creat_request(page)
        content=get_content(request)
        down_load(page,content)
