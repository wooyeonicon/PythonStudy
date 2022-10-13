# 作者 : 杨航
# 开发时间 : 2022/4/6 17:58
# 循环嵌套:测试乘法口诀
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end="\t")
    print("\n")
print("=========================")
a=1
b=1
while a<10:
    b=1
    while b<=a:
        print(str(a) + "*" + str(b) + "=" + str(a * b),end="\t")
        b+=1
    a += 1
    print("\n")
