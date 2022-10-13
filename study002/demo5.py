# 作者 : 杨航
# 开发时间 : 2022/4/3 0:40

# 数据类型 int float bool str

# 浮点类型不精确
n1 = 1.1
n2 = 2.2
print(n1+n2)

# 解决
from decimal import Decimal
print(Decimal(n1)+Decimal(n2))  # 这种也不精确
print(Decimal("1.1")+Decimal("2.2"))
print(Decimal("1.23")+Decimal("2.34"))

m = Decimal("1.1")+Decimal("2.2")
print(m)



