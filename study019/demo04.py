# 作者 : 杨航
# 开发时间 : 2022/10/10 18:11
# 将list作为堆栈

# 队列
list = [0,1,2,3,4]
def deque(n,list):
    list.append(n)
    del list[0]  # 删除第一位
    return list

for i in range(10,14):
    list = deque(i,list)
    print(list)

# 堆
list1 = [1,2,3,4]
def stack(n,list1):
    list1.append(n)
    list1.pop()
    return list1
print(stack(19,list1))