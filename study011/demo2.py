# 作者 : 杨航
# 开发时间 : 2022/4/11 20:56
# 函数的传递参数
def calc(a,b):
    c=a+b
    return c
print("位置传参")
result=calc(10,20)
print("关键字传参")
result1=calc(b=10,a=20)
print(result,result1)