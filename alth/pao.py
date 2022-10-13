# 作者 : 杨航
# 开发时间 : 2022/9/7 13:24
## 冒泡排序
a = [2,5,1,7,10,6,9,4,3,8]
# for i in range(10,0,-1):
#     for j in range(i-1):
#         if a[j] > a[j+1]:
#             t = a[j]
#             a[j] = a[j+1]
#             a[j+1] = t
# print(a)

# 递归排序（冒泡）升序
def pao(a,n):
    if n < 1:
        return a
    else:
        for i in range(n-1):
            if a[i] > a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
    pao(a,n-1)
pao(a,10)
print(a)