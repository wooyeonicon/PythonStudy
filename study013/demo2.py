# 作者 : 杨航
# 开发时间 : 2022/4/12 12:10
# 类的组成:类属性、实例方法、静态方法、类方法
class Student:
    native_pace='宝鸡'  # 直接写在类里的变量，成为类属性

    def __init__(self,name,age):    # 初始化函数
        self.name=name      # 赋值操作。self.name实体属性
        self.age=age


    def eat(self):      # 实例方法,必须加self
        print("学生吃饭...")

    @staticmethod       # 静态方法，静态方法不写self
    def method():
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    @classmethod        # 类方法
    def cm(cls):
        print("我是类方法")

# 在类之外定义的叫函数，在类之内定义的叫方法。
def drink():
    print("喝水")

# 创建对象
stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)
print("==调用方法==")
stu1.eat()
print(stu1.name)
print(stu1.age)
print("=======")
Student.eat(stu1)     # 与33行一致，都是调用方法

print("========类属性的使用=====")
print(Student.native_pace)
stu2=Student("李四",30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='西安'
print(stu1.native_pace)
print(stu2.native_pace)
print("=======类方法的使用方式=====")
Student.cm()
print("====静态方法的使用方式===")
Student.method()

