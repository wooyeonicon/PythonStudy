# 作者 : 杨航
# 开发时间 : 2022/4/4 20:35
# 选择条件
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
if a>=b:
    print(a,"大于等于",b)
else:
    print(a,"小于",b)
print("======使用条件表达式=====")
#  条件成立结果 if 条件 else 条件失败结果
print(str(a)+"大于等于"+str(b) if a>=b else str(a)+"小于"+str(b))