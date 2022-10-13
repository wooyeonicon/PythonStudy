# 作者 : 杨航
# 开发时间 : 2022/4/4 22:15
# for循环
for item in "Python":
    print(item)
for i in range(10):
    print(i)
for _ in range(5):
    print("人生苦短，我用python")
# 1-100的偶数和
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)