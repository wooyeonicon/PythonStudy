# 作者 : 杨航
# 开发时间 : 2022/4/4 11:21

# 比较运算符
a = 10
b = 10
print(a == b)  # 说明两个value相等
print(a is b)   # 说明两个id标识相等
list1 = [1,2,3,4]
list2 = [1,2,3,4]
print(list1 == list2)  # 说明两个value想等
print(list1 is list2)  # 说明两个id标识不相等
print(id(list1))
print(id(list2))
print(a is not b)
print(list1 is not list2)
