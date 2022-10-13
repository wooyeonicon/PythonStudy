# 作者 : 杨航
# 开发时间 : 2022/4/11 15:55
# 字符串操作的其他方法
s='hello,python'
print('replace()第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数')
print(s.replace('python','java'))
print(s.replace('python','java',2))
print('join()将列表或元组中的字符串合并成一个字符串')
list1=['hello','world','python']
print('|'.join(list1))
print(' '.join(list1))
t=('hello','world','python')
print(' '.join(t))
print('*'.join('Python'))
