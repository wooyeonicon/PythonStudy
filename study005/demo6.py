# 作者 : 杨航
# 开发时间 : 2022/4/4 23:01
# 循环
for item in range(3):
    pwd = input("请输入密码：")
    if pwd == "8888":
        print("密码正确")
        break
    else:
        print("密码错误")
else:
    print("三次密码错误")
print("=============else的其他两种用法=================")
a = 0
while a<3:
    pwd = input("请输入密码:")
    if pwd == "3333":
        print("密码正确")
        break
    else:
        print("密码错误")
else:
    print("三次密码错误")
