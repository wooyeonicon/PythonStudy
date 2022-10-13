# 作者 : 杨航
# 开发时间 : 2022/4/11 16:14
# 字符串的切片
s='hello,python'
s1=s[:5]   # 由于没有指定起始位置，默认从0开始
print(s1)
s2=s[6:]    # 由于没有设置终止位置，默认最后一位结束
s3='!'
newstr=s1+s3+s2
print(newstr)
print(id(s))
print(id(s1))
print('=============切片：[start:end:step]===========')
print(s[1:5:1])  # 不包含5
print(s[::-1])   # 反向
print(s[::2])  # 默认0开始，最后一位结束，步长为2
print(s[:-1])   # 注意
