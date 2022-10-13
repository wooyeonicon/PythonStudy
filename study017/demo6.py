# 作者 : 杨航
# 开发时间 : 2022/7/21 12:56
# 写文件
file=open('c.txt','a')
# file.write('hello')
lst=['java','python']
file.writelines(lst)
file.close()