# 作者 : 杨航
# 开发时间 : 2022/4/3 0:32

import keyword
print(keyword.kwlist)

# 保留字需要注意大小写

# 变量赋值
name = "张三"
print(name)
print("标识", id(name))
print("类型", type(name))
print("值", name)

# 多次赋值会发生变化
name = "李四"
print(name)
print("标识", id(name))
print("类型", type(name))
print("值", name)
