# 作者 : 杨航
# 开发时间 : 2022/10/10 18:03
# 匿名函数 lambda

# 案例1 (单个参数)
x = lambda a : a + 10
print(x(5))

# 案例2 （多个参数）
sum = lambda arg1,arg2 : arg1+arg2
print("相加后的值为:",sum(10,20))

# 案例3 （多个函数）
def myfunc(n):
    return lambda a : a * n
my1 = myfunc(2)
my2 = myfunc(3)
print(my1(10))
print(my2(10))