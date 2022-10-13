# 作者 : 杨航
# 开发时间 : 2022/4/8 14:21
# 字典生成式
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