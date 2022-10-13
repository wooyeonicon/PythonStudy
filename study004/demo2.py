# 作者 : 杨航
# 开发时间 : 2022/4/4 20:21
# 选择结构
m = 1000
i = int(input("请输入金额"))
if m>=i:
    m = m-i
    print("剩余金额为：", m)
else:
    print("余额不足")
print("============第一种写法==============")
score = int(input("请输入成绩："))
if score>=90 and score<=100:
    print("成绩优秀")
elif score>=80 and score<=89:
    print("成绩良好")
elif score>=60 and score<=79:
    print("成绩合格")
elif score>=0 and score<=59:
    print("成绩不合格")
else:
    print("成绩无效")

print("====第二种写法=======")
if 90<=score<=100:
    print("成绩优异")
elif 80<=score<=89:
    print("成绩良好")
else:
    print("成绩一般")