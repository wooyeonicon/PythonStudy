# 作者 : 杨航
# 开发时间 : 2022/4/12 15:34
# 动态绑定
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+'在吃饭')

stu1=Student("张三",20)
stu2=Student("李四",30)
print("=====动态绑定======")
# 比如：只给对象stu1添加一个性别属性，而stu2没有该属性，就需要动态绑定
print("====stu2动态绑定性别属性====")
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.age,stu2.name,stu2.gender)

print("=====动态绑定方法show()=====")
def show():
    print("定义在类之外的，称函数")
stu2.show=show  #  动态绑定方法
stu2.show()
