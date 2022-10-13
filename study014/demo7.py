# 作者 : 杨航
# 开发时间 : 2022/7/21 9:24
# 多态：具有多种形态，
# python为动态语言，崇尚“鸭子类型”，当一个动物走起来，和飞起来都像鸭子，那么就认为它是鸭子，只关心对象的行为，不关系对象的类型。
# Java为静态语言，多态的三个必要条件，继承、方法重写、父类引用指向子类对象
# 静态语言注重这种继承关系，动态语言只关注有没有这个方法。
class Animal(object):
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
class Person:  # Person类没有继承Animal类，还是可以被调用
    def eat(self):
        print("人吃饭")
# 定义一个函数
def fun(obj):
    obj.eat()
# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print("-----------")
fun(Person())    # Person类