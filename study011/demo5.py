# 作者 : 杨航
# 开发时间 : 2022/4/11 22:06
# 函数定义默认值参数
def fun(a,b=10):
    print(a,b)
fun(20)
fun(20,30)  # 传入的参数会将原来默认的参数进行覆盖
