# 作者 : 杨航
# 开发时间 : 2022/4/11 12:49
# 字符串操作：查询
s='hello.hello'
print('index()查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError')
print(s.index('lo'))
print('rindex()查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError')
print(s.rindex('lo'))
print('find()查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1')
print(s.find('lo'))
print('rfind()查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1')
print(s.rfind('lo'))