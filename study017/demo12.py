# 作者 : 杨航
# 开发时间 : 2022/7/23 10:44
# 列出指定目录下的所有.py文件
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):  # endswith以什么什么结尾
        print(filename)