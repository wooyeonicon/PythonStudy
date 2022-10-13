# 作者 : 杨航
# 开发时间 : 2022/4/12 0:34
# Bug : 异常处理机制
try:
    n1=int(input("请输入一个整数:"))
    n2=int(input("请输入另一个整数:"))
    result=n1/n2
    print("结果为:",result)
except ZeroDivisionError:
    print("除数不能为0哦！！！")
except ValueError:
    print("只能输入数字哦！！！")
print("程序结束")
