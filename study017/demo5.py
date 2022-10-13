# 作者 : 杨航
# 开发时间 : 2022/7/21 12:52
# 读文件
file=open('a.txt','r',encoding='utf-8')
# print(file.read())  # 全部读取
# print(file.read(2)) # 读取前两个字节
# print(file.readline())  # 读取一行，放在列表中
# print(file.readlines()) # 读取所有行，放在列表中
file.seek(2) # 指针跳过两个字节
print(file.read())
print(file.tell())  # 返回到最后一位的字节数
file.close()