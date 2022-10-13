# 作者 : 杨航
# 开发时间 : 2022/4/13 20:09
# 封装:age不希望在类的外部使用
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age     # 年龄不希望在类的外部被使用，所以加了两个__
    def show(self):        # 但是在内部方法中可以用
        print(self.name,self.__age)

stu=Student("张三",20)
stu.show()  # 这样调用者使用相当于在内部使用__age
print(stu.name)
# print(stu.__age)   age不希望在外部使用。
print(dir(stu))      # age不希望在外不使用，但是也可以使用，先用dir获取对象，然后直接输出属性
print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问
