# -*- coding:utf-8 -*-
# Author:Yatces


list1 = [1,4,5,4,8,9,6,3]
list1 = set(list1)

list2 = set([1,5,10,88,30,22])

print(list1,list2)

# 交集
print(list1.intersection(list2))
print(list1&list2)


# 并集
print(list1.union(list2))
print(list1|list2)

# 保留list1  list2里面没有
print(list1.difference(list2))
print(list1-list2)

# 子集
list3 = set([1,5])
print(list3.issubset(list1),list3.issubset(list2))
print(list1.issuperset(list3),list2.issuperset(list3))


# 对称差集
print(list1.symmetric_difference(list2))


# 有交集为False 无交集为True
list4 = set([45,96,100,13])
print(list2.isdisjoint(list4))





