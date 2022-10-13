# 作者 : 杨航
# 开发时间 : 2022/4/8 11:25
# 获取字典的元素
score = {"张三":100,"李四":98,"王五":90}
print("=====第一种方式，使用[]=======")
print(score["张三"])
print("========第二种方式，使用get()===========")
print(score.get("张三"))

print("========两种方式的区别==========")
print(score.get("柽柳"))  # None
print(score["柽柳"])   # 爆错，KeyError
