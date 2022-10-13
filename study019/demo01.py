# 作者 : 杨航
# 开发时间 : 2022/10/10 17:39
# 推导式
# python支持各种数据类型的推导式：list dict set tuple

# 1.列表推导式
# [表达式 for 变量 in 列表]| [表达式 for 变量 in 列表 if 条件]
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names) # 可以加if，也可以不加

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 2.字典推导式
items=["zhang","li","wang"]
scores=[90,98,99]
d = {item:score for item,score in zip(items,scores)}
print(d)
print("============key转换为大写==============")
d1 = {item.upper():score for item,score in zip(items,scores)}
print(d1)
print("=============当两个列表大小不同时，按数量小的来确定数量==============")
i1=["zhan","li"]
s1=[90]
d2 = {item:score for item,score in zip(i1,s1)}
print(d2)
i2=["zhang"]
s2=[90,98]
d3={item:score for item,score in zip(i2,s2)}
print(d3)

# 3.集合推导式
print("===集合生成式==")
s1={i*i for i in range(10)}
print(s1)  #  元素是无序的

# 4.元组推导式
a = (x for x in range(1,10))
print(tuple(a))