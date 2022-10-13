# 作者 : 杨航
# 开发时间 : 2022/4/2 23:39

# 标识符：字母、数字和下划线组成，必须由下划线或字母开头。
# python中的，每个对象都包含是三个基本要素：id、type、value
# 进制：0b二进制、0o八进制、0x十六进制
# 数据类型：简单类型：（整数类型、实数类型、布尔类型、复数类型）
#          序列：（列表、元组、字符串）
#         其他类型：（字典、集合）
# x=3+2j     x.real、 x.imag



# 输出字符串
print("Hello World!")

# 输出数字
print(520)

print(3+1)    # 输出运算符

x = 3+2j
print(x.real)
print(x.imag)

# 输出的数据放在文件中
fp = open("D:/test.txt", "a+")
print("Hello World!", file=fp)
fp.close()



# 输出不换行
print("hello", "world", "python")

