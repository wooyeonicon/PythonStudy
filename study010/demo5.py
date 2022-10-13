# 作者 : 杨航
# 开发时间 : 2022/4/11 13:25
# 字符串分割 split(),rsplit()
s='hello world python'
print('split()从字符串的左边开始分割，默认的分隔符为空格，返回的值是一个列表。')
list1=s.split()  # 没有指令分隔符，默认为空格
print(list1)

print('split(sep)带参数')
s1='hello|world|python'
print(s1.split('|'))
print(s1.split(sep='|'))

print(s1.split(sep='|',maxsplit=1))  # 从左侧最大分一次

print(s1.rsplit(sep='|',maxsplit=1))  # 从右侧最大分一次