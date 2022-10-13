# 作者 : 杨航
# 开发时间 : 2022/4/12 0:19
# 函数作用域
print("局部变量")
def fun(a,b):  # 局部变量
    c=a*b
    print(c)
print("全局变量")
name='杨航'
print(name)
def fun1():
    print(name)
fun1()
print("局部变量设置为全局变量")
def fun2():
    global age  # 设置全局变量
    age=20
    print(age)
fun2()
print(age)
