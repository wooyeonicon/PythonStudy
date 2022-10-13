# 作者 : 杨航
# 开发时间 : 2022/4/6 18:39
# 列表查询
print("==========列表中查询某元素的index==========")
list1 = ["hello","world",98,"hello"]
print(list1.index("hello"))  # 如果列表中有重复元素，则只返回第一次出现的元素的index
#print(list1.index("Python"))  # 报错
print("======从指定的段中查询=======")
print(list1.index("hello",1,4))  # start=1,stop=4,并且不包含stop

print("=======从列表中获取某一元素=========")
print(list1[2])
print(list1[-1])