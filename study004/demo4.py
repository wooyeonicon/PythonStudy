# 作者 : 杨航
# 开发时间 : 2022/4/4 20:45
# 总结
age = int(input("请输入您的年龄："))
if age:
    print(age)
else:
    print("年龄为：",age)
# 可以用对象直接作为判断条件，0的布尔值为False

a = dict()
if a:
    print("1")
else:
    print("0")