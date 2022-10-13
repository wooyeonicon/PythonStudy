# 作者 : 杨航
# 开发时间 : 2022/7/23 10:20
# with语句（上下文管理器）：可以自动管理上下文资源，不论什么原因跳出with块，都
# 能确保文件正确的关闭，以此来达到释放资源的目的
with open("a.txt",'r',encoding='utf-8') as file:
    print(file.read())