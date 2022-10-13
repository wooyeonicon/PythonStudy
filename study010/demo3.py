# 作者 : 杨航
# 开发时间 : 2022/4/11 13:02
# 字符串的大小写转换操作
s='hello,world,Python'
print('upper把字符串中所有字符都转成大写字母')
print(s.upper())
print('lower()把字符串中所有字符都转成小写字母')
print(s.lower())
print('swapcase()把字符串中所有大写字母转成小写，把所有小写转成大写')
print(s.swapcase())
print('capitalize()把第一个字符转为大写，把其余字符转成小写')
print(s.capitalize())
print('title()把每个单词的第一个字符转换为大写，把每个单词的剩余字符转成小写')
print(s.title())

print('==注意==')
s1 = 'python'
print(id(s1),id(s1.lower()))  # 字符串转换之后，会产生一个新的字符串对象（与值无关）
print(s1==s1.lower())    # True
print(s1 is s1.lower())  # False
