# 作者 : 杨航
# 开发时间 : 2022/4/7 0:32
# 向列表中添加元素：append(),extend(),insert(),切片
list1 = [1,2,3]
print("==========使用expend()========")
list1.append("python")
print(id(list1))
print(list1)  # 对象没变
print(id(list1))
print("============使用extend()==============")
list2 = ["hello","world"]
# list1.append(list2)  # 会将list2作为一个元素添加到后面
list1.extend(list2)
print(list1)
print(id(list1))
print("============使用insert()==============")
list1.insert(1,90)
print(list1)
print("=======使用切片============")
list1[1:] = list2
print(list1)