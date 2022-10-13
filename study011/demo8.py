# 作者 : 杨航
# 开发时间 : 2022/4/12 0:01
# 函数参数的总结
def fun(a,b=10):  # b是在函数的定义处，所以b是形参，而且进行了赋值，所以b成为默认值形参
    print('a=',a)
    print('b=',b)
def fun2(*args):  # 个数可变的位置形参
    pass
def fun3(**args):  #个数可变的关键字形参
    pass
fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44)

def fun4(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
# 调用fun4函数
fun4(10,20,30,40)  # 位置实参传递
fun4(a=10,b=20,c=30,d=40)  # 关键字实参传递
fun4(10,20,c=30,d=40)

def fun5(a,b,*,c,d):  # 从*之后，所有的参数都必须通过关键字传递参数
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
fun5(10,20,c=30,d=40)

'''函数定义时的形参的顺序问题：'''
def fun6(a,b,*,c,d,**args):
    pass
def fun7(*args,**args1):
    pass
def fun8(a,b=10,*args,**args1):
    pass