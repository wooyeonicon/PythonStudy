# 作者 : 杨航
# 开发时间 : 2022/4/8 0:18
# 列表的排序 sort()、sorted()

print("========sort()方法：由小到大排序，不产生新的列表对象============")
list1 = [1,21,2,1,121,45]
list1.sort()
print(list1)  # 是在原来列表上进行的排序，而不是创建一个新的列表

print("=====sort():降序排序=======")
list1.sort(reverse=True)  # reverse=True为降序，默认reverse=False
print(list1)

print("========sorted():使用内置函数进行排序,将产生一个新的列表对象===========")
list2 = sorted(list1)
print(list2)
print("===========sorted()降序==========")
list3 = sorted(list1,reverse=True)
print(list3)
