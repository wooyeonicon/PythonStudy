# 作者 : 杨航
# 开发时间 : 2022/4/11 21:17
# 函数的返回值:返回多个返回值时，为元组
def fun(num):
    odd=[] # 存奇数
    even=[]  # 存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(fun([10,29,34,23,44,53,55]))
'''
函数的返回值：
    1.如果函数没有返回值，return可以省略不写
    2.函数的返回值，如果是1个，直接返回类型
    3.函数的返回值，如果是多个，返回的结果为元组
'''
print('=====无参数传入====')
print("===1===")
def fun1():
    print('hello')
fun1()
print('===2===')
def fun2():
    return 'hello'
res=fun2()
print(res)
print('===3===')
def fun3():
    return 'hello','world'
print(fun3())
'''
函数在定义时，是否需要返回值，看情况
'''