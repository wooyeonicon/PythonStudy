# 作者 : 杨航
# 开发时间 : 2022/4/12 0:24
# 函数递归
def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)
print(fun(6))
