# 作者 : 杨航
# 开发时间 : 2022/4/11 0:42
# 集合的数学操作：交集、并集、差集、对称差集
# 差集：整个B-AB的交集
# 对称差集: AB交集-AB并集
s1={1,2,3,4}
s2={1,2,3,5,6}
print("==交集==")
print(s1.intersection(s2)) # 第一种
print(s1 & s2)  # 第二种

print(s1)
print(s2)  # 都不会变化
print("==并集==")
print(s1.union(s2))  # 第一种
print(s1 | s2)  # 第二种

print(s1)
print(s2)  # 都不会变化

print("==差集===")
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)

print(s1)
print(s2)  # 都不会变化

print("==对称差集==")
print(s1.symmetric_difference(s2))
print(s1^s2)


