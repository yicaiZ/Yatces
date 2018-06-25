# -*- coding:utf-8 -*-
# Author:Yatces

# {}是指字典  []是指列表  ()是指元组
# info = {
#     "test001":[("aaa","bbb"),("ccc","ddd")],
#     "test002":[("eee","fff"),("hhh","iii")]
# }

# 查找
# print(info["test001"][0][1])
# print(info.get("test001")[0][1])

# 修改
# info.get("test001")[0][0] = "jjj"
# print(info)

# 循环遍历字典
# for i in info:
#     print(i,info[i])
# print('---------------------')
# for k,v in info.items():
#     print(k,v)




# 创建dict
# d1 = dict(a=1, b=2, c=2)
# d2 = dict([('a',1), ('b',2), ('c',3)])
# d3 = dict({'a':1,'b':2, 'c':3})
#
# print('d1',d1)
# print('d2',d2)
# print('d3',d3)


# 1. clear(清空字典内容)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# print(stu.clear())# 输出：None


# 2. copy（拷贝字典）
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# stu2 = stu.copy()
# print(stu2)


# 3. fromkeys(指定一个列表，把列表中的值作为字典的key, 生成一个字典)
name = ['tom', 'lucy', 'sam']
print(dict.fromkeys(name))  #输出：{'tom': None, 'lucy': None, 'sam': None}
print(dict.fromkeys(name, 25))  # 指定默认值 {'tom': 25, 'lucy': 25, 'sam': 25}


# 4. get(指定key，获取对应的值)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# print(stu.get('num2'))  # 输出：Lucy


# 5. items(返回由“键值对组成元素“的列表)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# print(stu.items())  # 输出：dict_items([('num2', 'Lucy'), ('num3', 'Sam'), ('num1', 'Tom')])


# 6.keys(获取字典所有的key)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# print(stu.keys())  # 输出：dict_keys(['num3', 'num1', 'num2'])



# 7. pop(获取指定key的value，并在字典中删除)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# name = stu.pop('num2')
# print(name, stu) # 输出：Lucy {'num1': 'Tom', 'num3': 'Sam'}


# 8. popitem(随机获取某个键值对，并在字典中删除)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# name = stu.popitem()
# print(name, stu)  # 输出：('num2', 'Lucy') {'num3': 'Sam', 'num1': 'Tom'}


#  9. setdefault(获取指定key的value，如果key不存在，则创建)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# name = stu.setdefault('num5')
# print(name, stu)   # 输出：None {'num1': 'Tom', 'num2': 'Lucy', 'num5': None, 'num3': 'Sam'}


# 10.  update(添加键 - 值对到字典)
# stu = {
#     'num1': 'Tom',
#     'num2': 'Lucy',
#     'num3': 'Sam',
# }
# stu.update({'num4': 'Ben'})
# print(stu)    # 输出：{'num2': 'Lucy', 'num3': 'Sam', 'num1': 'Tom', 'num4': 'Ben'}











