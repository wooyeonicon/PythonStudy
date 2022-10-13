# 作者 : 杨航
# 开发时间 : 2022/4/11 16:58
# 格式化字符串
print("==第一种==")
name='张三'
age=30
print('我叫%s,今年%d岁' % (name,age))
print("===第二种 ==")
print('我叫{0},今年{1}岁'.format(name,age))
print("==第三种 f-string==")
print(f'我叫{name},今年{age}岁')
