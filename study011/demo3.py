# 作者 : 杨航
# 开发时间 : 2022/4/11 21:09
# 函数调用的参数传递
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    return
n1=11;
n2=[22,33,44]
fun(n1,n2)
print('n1',n1)
print('n2',n2)
'''在函数调用过程中，进行参数的传递，
如果是不可变对象，在函数体的修改下不会影响实参的值
如果是可变对象，在函数体的修改下回影响实参的值
'''