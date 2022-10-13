# 作者 : 杨航
# 开发时间 : 2022/4/11 0:28
# 集合之间的关系
print("==判断两个集合是否相等===")
s1={1,2,3,4}
s2={4,3,2,1}
print(s1==s2)
print(s1 is s2)
print(s1!=s2)
print("====判断一个集合是否是另一个集合的子集=====")
s3={1,2}
print(s3.issubset(s2)) # 判断s3是s2的子集
print("====判断一个集合是否是另一个集合的超集===")
print(s2.issuperset(s3))
print("===两个集合中是否有交集===")
s4={1,2,3,5}
print(s4.isdisjoint(s2))  # 没有交集为True
