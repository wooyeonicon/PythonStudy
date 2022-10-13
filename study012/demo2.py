# 作者 : 杨航
# 开发时间 : 2022/4/12 0:50
# try-except-else:
try:
    a=int(input("请输入第一个整数:"))
    b=int(input("请输入第二个整数:"))
    result=a/b
except BaseException as e:
    print("出错了",e)
else:
    print("计算结果为:",result)
