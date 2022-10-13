# 作者 : 杨航
# 开发时间 : 2022/4/11 11:03
# 字符串驻留机制
print("==字符串驻留机制==")
a="python"
b="python"
c="python"
print(id(a),id(b),id(c))
print("字符串长度为0或1时，驻留机制")
d='123%'
e='123%'
print(d is e)  # pycharm对字符串进行了优化
print(a is b)
