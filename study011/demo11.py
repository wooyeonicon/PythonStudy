# 作者 : 杨航
# 开发时间 : 2022/4/12 0:26
# 斐波那锲数列
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
print(fun(6))
print("===输出前6项===")
# 输出前六位数字
for i in range(1,7):
    print(fun(i))