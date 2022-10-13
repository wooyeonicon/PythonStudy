# 作者 : 杨航
# 开发时间 : 2022/4/4 22:08
# 计算1-100之间偶数和 与 奇数和
print("=====第一种方法======")
b = 1
sum = 0
while b<=100:
    if b%2==0:
        sum+=b
    b+=1
print(sum)
print("======第二种方法======")
a = 1
sum1 = 0
while a<=100:
    if a%2:        # a%2=0的时候是False,所以进不去，所以为奇数和
        sum1+=a
    a+=1
print("奇数和为：",sum)

c = 1
sum2 = 0
while c<=100:
    if not bool(c%2):
        sum2+=c
    c+=1
print("偶数和为：",sum2)