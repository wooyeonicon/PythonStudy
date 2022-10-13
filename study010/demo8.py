# 作者 : 杨航
# 开发时间 : 2022/4/11 16:06
# 字符串比较:一位一位比较
print('apple'>'app')  # True
print('apple'>'banana')  # False
print(ord('a'),ord('b'))

print(chr(97),chr(98))

print('*** == 与is的区别****')
print('==比较的是value')
print('is比较的是id')
a=b='python'
c='python'
print(a==b)
print(a==c)
print(a is b)  # 比较内存地址
print(a is c)
