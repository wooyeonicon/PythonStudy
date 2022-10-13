# 作者 : 杨航
# 开发时间 : 2022/4/10 23:37
# 元组特性
t = (10,[10,20],30)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
print("尝试将t[1]修改为100")
print(id(100))
#t[1] = 100  #  元组是不允许修改元组的类型

print("由于[10,20]列表，而列表是可变序列，所以可以向列中添加元素，而列表的内存地址不变")
t[1].append(100)
print(t[1])
print(t[1],type(t[1]),id(t[1]))

