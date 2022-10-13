# 作者 : 杨航
# 开发时间 : 2022/4/8 11:32
# key的判断
print("========key是否存在========")
score = {"张三":90,"李四":98,"王五":78}
print("张三" in score)
print("张三" not in score)

print("========删除指定的Key-value======")
del score["张三"]
print(score)
print("=======清空字典===========")
score.clear()
print(score)
print("=========字典的新增key-value===========")
score["柽柳"]=99
print(score)
print("=========修改========")
score["柽柳"]=100
print(score)
