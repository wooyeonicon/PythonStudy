# 作者 : 杨航
# 开发时间 : 2022/4/4 20:48
# 内置函数range
print("======第一种使用方式：range(stop) 整数序列，每次增加1=======")
r = range(10)
print(list(r))
print("======第二种使用方式:range(start,stop) 默认不包含stop,步长为1======")
s = range(1,10)
print(list(s))
print("========第三种使用方式：range(start,stop,step) ，步长step=======")
w = range(1,10,2)
print(list(w))
# 判断一个数是否在序列中
print(10 in w)
print(10 not in w)
