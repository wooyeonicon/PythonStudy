# 作者 : 杨航
# 开发时间 : 2022/4/10 22:36
# 元组tuple的创建 3种
print("=========第一种======")
t=('python','world',90)
print(t)
print(type(t))

print("======第二种：内置函数tuple======")
t1 = tuple(('python','world',90))
print(t1)
print(tuple(t1))

print("==========第三种：省略括号=======")
t2 = 'python',90,'world'
print(t2)
print(type(t2))
print("=======***如果只有一个元素，括号不能省略,并且需要,========")
t3 = ('python',) # 如果不加, 是str类型
print(type(t3))

print("三种类型的空创建")
list1=[]
list2 = list()

d1 = {}
d2 = dict()

tt1 = ()
tt2 = tuple()
print("1.",list1,list2,"2.",d1,d2,"3.",tt1,tt2)
