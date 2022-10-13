# 作者 : 杨航
# 开发时间 : 2022/7/21 9:57
# 特殊方法： __len__():通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
#          __add__():通过重写_add_()方法，可使用自定义对象具有“+”功能
#          __new__():用于创建对象
#          __init__():对创建的对象进行初始化
a=20
b=100
c=a+b  # 两个整数类型的对象相加
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student("张三")
stu2=Student("李四")
s=stu1+stu2  # 实现两个对象相加（因为在类中，编写了__add__()）
print(s)
s=stu1.__add__(stu2)  # 在类中必须重写__add__()
print(s)

print("-----------")
lst=[1,2,3,4]
print(len(lst))  # len是内置函数
print(lst.__len__())
print(len(stu1))