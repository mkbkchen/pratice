from bs4 import BeautifulSoup

#通过解析本地文件，来将bs4的基础语法进行讲解
    #默认打开的文件编码格式是gbk，所以打开文件的时候需要指定编码
soup=BeautifulSoup(open('22、解析_bs4的基本使用.html', encoding='utf-8'), 'lxml')
print(soup)

#bs4的基本语法
#一、根据标签名查找节点
    #注意：找到的是第一个符合条件的数据
print(soup.a)
    #返回的是标签的属性和属性值
print(soup.a.attrs)
#二、bs4的一些函数
#(1)find
print(soup.find('a')) #返回第一个符合条件的数据
print(soup.find('a',title="a2")) #根据title的值来找到对应的标签对象
print(soup.find('a',class_="a1")) #根据class的值来找到对应的标签对象，注意的是class_避免与python自带的重复
#(2)find_all
print(soup.findAll('a')) #返回的是一个列表，并且返回所有的a标签
print(soup.findAll(['a','span'])) #如果想获取多个标签，需要在findall标签中添加列表的数据
print(soup.findAll('li',limit=2))#limit是查找前几个数据
print('......')

#(3)select（推荐）
print(soup.select('a')) #返回的是一个列表，并且返回所有的a标签
    #1、类选择器
print(soup.select('.a1')) #可以通过.代表class，这种操作叫做类选择器
print(soup.select('#l1'))  ##代表id
    #2、属性选择器——通过属性来寻找对应的标签
        #查找到li标签中有id的标签
print(soup.select('li[id]'))
        #查找到li标签中id为l2的标签
print(soup.select('li[id="l2"]'))
    #3、层级选择器
        #后代选择器——找到的是div下面的li
print('////////')
print(soup.select('div li'))
        #子代选择器——某标签的第一级子标签
print('aaaaaaaa')
print(soup.select('div>ul>li'))  #很多的计算机编程语言中不加空格会报错，bs4中不会报错

    #找到a标签和li标签的所有的对象
print(soup.select('a,li'))
print('^^^^^^^^^^')

#三、节点信息
#（1）获取节点内容——如果标签对象中只有内容，那么string和getText都可以
    #如果标签对象中还有标签，那么string就获取不到数据
obj=soup.select('#d1')[0] #select返回的是列表，列表不能用string
print(obj.string)
print(obj.getText()) #推荐
print(',,,,,,,,')
#（2)节点的属性
obj=soup.select('#p1')[0]
print(obj.name) #name是标签的名字
print(obj.attrs) #attrs将属性值作为一个字典返回
print('。。。。。。')
#（3）获取节点的属性
obj=soup.select('#p1')[0]
print(obj.attrs.get('class')) #获取class的内容，获取字典的值用get
print(obj.get('class'))




