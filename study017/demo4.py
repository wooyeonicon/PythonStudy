# 作者 : 杨航
# 开发时间 : 2022/7/21 12:47
# 文件分为两大类：文本文件和二进制文件
# 文本文件：存储的是普通字符文本，默认为unicode字符集，可以使用记事本程序打开
# 二进制文件：把数据内容用字节进行存储，无法用记事本打开，必须使用专用的软件打开，比如音频、图片、doc文档等
src_file=open('logo.PNG','rb')
target_file=open('copylogo.PNG','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()