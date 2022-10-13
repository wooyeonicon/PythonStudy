# 作者 : 杨航
# 开发时间 : 2022/4/8 14:35

# 元组，字符串：不可变序列
# 元组：t=('python',90,20.1)
# 列表、字典:可变序列
list1 = [10,20,30]
print(id(list1))
list1.append(40)
print(id(list1))

s = 'hello'
print(id(s))
s = s+'world'
print(id(s))