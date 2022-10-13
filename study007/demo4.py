# 作者 : 杨航
# 开发时间 : 2022/4/8 11:38
# 获取字典视图 1.keys()获取字典中的所有key,2.values()获取字典中所有value
# 3.items()获取字典中所有key-value对
score={"张三":90,"李四":98,"王五":99}
print("==========获取所有的键=============")
keys = score.keys()
print(keys)
print(type(keys))
print("=========将keys转换成列表=========")
print(list(keys))  # 将所有的key组成的视图转成列表
print("===========获取所有的value========")
values = score.values()
print(values)
print(type(values))
print(list(values))
print("========获取所有的key-value=========")
items = score.items()
print(items)
print(list(items))    # ('张三', 90)元组
