# 作者 : 杨航
# 开发时间 : 2022/4/10 23:50
# 集合创建
print("===第一种==")
s={2,2,3,4,5,6,5,7} # 集合中的元素不能重复，重复的输出会出现一个
print(s)

print("==第二种===")
s1 = set(range(6))
print(s1,type(s1))

print("===第三种===")
s2 = set([3,4,23,34,3,2,4])  # 将列表转换为set集合
print(s2,type(s2))

print("=====第四种===")
s3 = set((1,23,23,4))  # 将元组转换为set集合
print(s3,type(s3))   # 集合中的元素是无序的

print("===第四种===")
s4 = set("python")   # 将字符串列表转换为set集合
print(s4,type(s4))  # 无序的

print("===第五种==")
s5 = set({1,2,34,2,3,1,3})  # 将集合设置成集合
print(s5)

print("设置空集合")
s6 = {};
print(s6,type(s6))  # 是空字典，而不是空集合
s7 = set()
print(s7,type(s7))

