# 作者 : 杨航
# 开发时间 : 2022/10/10 18:20
# 字典遍历
# 1.items():字典遍历
dict = {1:'a',2:'b',3:'4'}
for k,v in dict.items():
    print(k,v)

# 2.enumerate():序列遍历中，索引位置和对应值同时得到
for i,v in enumerate(['a','b','c']):
    print(i,v)

# 3.zip():同时遍历两个或多个序列
list1 = ['a','b','c','d']
list2 = [1,2,3,4]
for i,j in zip(list1,list2):
    print(i,j)

# 4.reversed()：反向遍历
for i in reversed(range(1,10,2)):
    print(i)