from lxml import etree

#xpath解析
#（1）本地文件                                             etree.parse


#（2）服务器响应的数据  response.read(),decode('utf-8') ***  etree.HTML()

#xpath解析本地文件
tree=etree.parse('解析xpath的基本使用.html')
print(tree)

#tree.xpath('xpath')路径

#(1)路径查询——查找ul下面的li：/代表子节点  //代表子孙节点

li_list=tree.xpath('//body/ul/li')
    #判断列表的长度
print(li_list)
print(len(li_list))

#(2)谓词查询
    #查找有id属性的li标签
    #text()获取标签中的内容
li_list2=tree.xpath('//ul/li[@id]/text()')
print(li_list2)
    #查找id属性为l1的li标签、需注意单引号里面需要是双引号的问题
li_list3=tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list3)

#（3）属性查询
    #查找到id为l1的标签的class属性值
li=tree.xpath('//ul/li[@id="l1"]/@class')
print(li)
#（4）模糊查询
    #查找id里面包含l的li标签
li_list4=tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list4)
    #查找id的值以c开头的标签
li_list5=tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(li_list5)


#（5）内容查询

#（6）逻辑查询
    #查询id为l1和class为c1的
li_list6=tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
print(li_list6)

li_list7=tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text() ')
print(li_list7)