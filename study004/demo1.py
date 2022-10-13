# 作者 : 杨航
# 开发时间 : 2022/4/4 19:53
# python一切都是对象，所有对象都有一个布尔值。
# 对象的布尔值 bool()
# False,数值0,None,空字符串,空列表,空元组,空字典,空集合（都为False）
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(""))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))   # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
print("========================")
print(bool(123))

a = dict()
if bool(a):
    print("1")
else:
    print("0")

if a is None:
    print("1")
else:
    print("0")

if a == None:
    print("1")
else:
    print("0")

