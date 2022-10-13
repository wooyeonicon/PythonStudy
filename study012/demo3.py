# 作者 : 杨航
# 开发时间 : 2022/4/12 0:54
# try-except-else-finally
try:
    a=int(input("请输入第一个整数:"))
    b=int(input("请输入第二个整数:"))
    result=a/b
except BaseException as e:
    print("出错了",e)
else:
    print("计算结果为:",result)
finally:
    print("无论是否产生异常，总会被执行的代码")
print("程序结束")
