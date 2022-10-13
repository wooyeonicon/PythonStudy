# 作者 : 杨航
# 开发时间 : 2022/4/6 18:26
# 列表的创建：两种方式(列表中的元素类型可以不同)
print("==========第一种创建==========")
list1 = ["hello","world",89]
print(list1)
print("==========第二种创建=========")
list2 = list(["hello","world",90])
print(list2)
print("输出第一个位置上的元素：",list2[0],list2[-3])
