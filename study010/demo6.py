# 作者 : 杨航
# 开发时间 : 2022/4/11 13:34
# 判断字符串
s='hello,world'
print('isidentifier()判断指定的字符串是否是合法的标识符')
print(s.isidentifier())  # 合法标识符：数字，字母和下划线组成的
print('hello'.isidentifier())
print('张三'.isidentifier())
print('isspace()判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）')
print(s.isspace())
print('\t'.isspace())
print('isalpha()判断指定的字符串是否全部由字母组成')
print('abc'.isalpha())
print('张三'.isalpha())
print('isdecimal()判断指定字符串是否全部由十进制的数字组成')
print('123'.isdecimal())
print('123四'.isdecimal())
print('isnumeric()判断指定的字符串是否全部由数字组成')
print('123'.isnumeric())
print('123四'.isnumeric())
print('isalnum()判断指定字符串是否全部由字母和数字组成')
print('abc1'.isalnum())
print('张三123'.isalnum())  # True
print('abc!'.isalnum())