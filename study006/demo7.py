# 作者 : 杨航
# 开发时间 : 2022/4/7 23:51
# 删除列表中的元素
list1 = [1,2,3,4,5,6,3]
list1.remove(3)  # remove(),一次删除一个元素，重复元素只删除第一个remove()中的参数是list中元素，而不是index
print(list1)

list1.pop(1)   # pop()，删除指定位置上的数据，传的参数是index
print(list1)
list1.pop()  #pop()，如果没有参数会删除list中最后一个数据
print(list1)

print("==========切片操作，至少删除一个元素，会产生一个新的列表对象============")
list2 = list1[1:3]
print(list2)

print("=======不产生新的列表对象，而是删除原列表中的内容========")
list1[1:3] = []
print(list1)

print("=======清除列表中的所有元素========")
list1.clear()
print(list1)
print("=========删除整个列表===========")
del list2
print(list2)
