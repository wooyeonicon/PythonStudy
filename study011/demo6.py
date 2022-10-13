# 作者 : 杨航
# 开发时间 : 2022/4/11 23:37
# 函数参数不确定的情况
def fun(*args):  # 参数个数只能是一个
    print(args)
    print(args[0])
fun(10)
fun(10,20)
fun(10,20,30)

def fun1(**args):   # 参数个数只能是一个
    print(args)
fun1(a=10)
fun1(a=10,b=20)
fun1(a=10,b=20,c=30)
print('在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参前面')
def fun3(*agrs,**args1):
    print(agrs)
    print(args1)
