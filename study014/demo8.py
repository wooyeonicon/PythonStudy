# 作者 : 杨航
# 开发时间 : 2022/7/21 9:37
# 特殊属性
# 特殊属性: __dict__:获得类对象或实例对象所绑定的所有属性和方法的字典

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class D(A,B):
    pass
# 创建C类的对象
c=C("张三",20)   # c是C类的一个实例对象
print(c.__dict__)   # 实例对象的属性字典
print(C.__dict__)   # 类对象的方法字典
print("--------------")
print(c.__class__) # 输出了对象所属的类
print(C.__bases__) # C类的父类类型的元素
print(C.__base__) # C类最近的一个父类，谁写在前边，谁最近（类的基类）
print(C.__mro__) # 类的层次结构
print(A.__subclasses__())  # A类的子类列表


