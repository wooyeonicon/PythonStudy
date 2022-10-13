# 作者 : 杨航
# 开发时间 : 2022/9/14 12:03
# n皇后：n*n棋盘上，放置n个皇后，要求每个皇后不同行、不同列、不同左右对角线

# 实践6皇后
# 以列递归

# 行代表下标
# 列代表值
# a=[]
# # 检查该数是否可以存放
# def check(a,j):  # a结果、j当前要检查的数字
#    if len(a) > 0:
#       for i in range()
#
#
# # 选择第一个皇后的位置
# def first(n):
#    if len(a) == 0:
#       for i in range(n):
#          a.append(i)
#
#
# # 从一行中选出符合的列
# def choose(n):
#    for j in range(n):
#       for m in range(len(a)):
#          if j != a[m] and j != a[m] + 1 and j != a[m] - 1:
#             a.append(j)
#             break
#    return a
#
# def nqueen(n):
#    flag=0
#    for i in range(n): # 行
#       for j in range(n):   # 列
#          if flag==1:
#             print('lll')
#             break
#
#          if len(a) == 0:
#             a.append(j)
#             print('列',j)
#             break
#          if len(a) != 0:
#             for m in range(len(a)):
#                if j!=a[m] and j!=a[m]+1 and j!=a[m]-1:
#                   a.append(j)
#                   flag=1
#                   break
#    return a
# nqueen(6)
# print(a)


