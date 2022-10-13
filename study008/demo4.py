# 作者 : 杨航
# 开发时间 : 2022/4/10 23:45
# 元组的遍历，元组是可迭代对象，所以可以使用for..in进行遍历
t=(90,80,20,"python")
print("第一种获取元组元素的方式，使用索引")
print(t[0])
print(t[1])
print(t[2])
print(t[3])

print("遍历元组")
for item in t:
    print(item)

