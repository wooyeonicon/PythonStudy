# 作者 : 杨航
# 开发时间 : 2022/7/23 10:35
# os模块操作目录
import os
print(os.getcwd())  # 返回当前的工作目录
os.listdir('')  # 返回指定路径下的文件和目录信息
os.mkdir() # 创建目录
os.makedirs()  # 创建多级目录
os.rmdir('')  # 删除目录
os.removedirs('')  # 删除多级目录
os.chdir('')  # 将path设置为当前工作目录

