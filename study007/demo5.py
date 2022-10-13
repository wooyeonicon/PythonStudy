# 作者 : 杨航
# 开发时间 : 2022/4/8 14:12
# 字典元素的遍历
score={"张三":90,"李四":98,"王五":99}
for item in score:
    print(item,score[item],score.get(item))