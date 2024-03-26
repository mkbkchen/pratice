import json
import jsonpath

obj=json.load(open('20、解析_jsonpath.json', 'r', encoding='utf-8'))
print(obj)
#书店所有的书的作者
author_list1=jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author_list1)

#所有的作者
author_list2=jsonpath.jsonpath(obj,'$..author')
print(author_list2)

#store的所有元素
store_list=jsonpath.jsonpath(obj,'$.store.*')
print(store_list)

# store里面所有的price
price_list=jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

#第三个书
third_book=jsonpath.jsonpath(obj,'$..book[2]')
print(third_book)
#最后一本书
last_book=jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
print(last_book)

#前两本书
first_two_book=jsonpath.jsonpath(obj,'$..book[:2]')
print(first_two_book)

#条件过滤需要在（）前面加？
    #过滤出所有包含isbn的书
isbn_list=jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(isbn_list)
    #哪本书超过了10块钱
ten_book=jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(ten_book)


