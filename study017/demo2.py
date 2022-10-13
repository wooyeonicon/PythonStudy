# 作者 : 杨航
# 开发时间 : 2022/7/21 12:30
# 读取文件的内容
file=open('a.txt','r',encoding='utf-8')
print(file.readlines())  # 结果为列表
file.close()