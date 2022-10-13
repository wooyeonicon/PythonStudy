# 作者 : 杨航
# 开发时间 : 2022/4/7 0:05
# 列表查询多个元素
list1 = [1,2,3,4,5,6,7]
print(list1[1:6:1])  # [start:stop:step]  不包含stop,step默认为1
print("原列表",id(list1))
list2 = list1[1:6:1]
print("切的新列表",id(list2))  # 切出的列表会重新创建一个地址，成为新列表（不是原来的列表）
print("=============步长为正数===================")
print(list1[1:6])
print(list1[1:6:])
print(list1[:6:1])  # start默认为0
print(list1[1::2])  # stop默认为最后一位
print("===============步长为负数============")  # 注意不包含stop
print(list1[::-1])  # 相当于逆序
print(list1[7::-1])
print(list1[6::-1])