# 作者 : 杨航
# 开发时间 : 2022/4/13 20:01
# 面向对象的三大特征：继承、封装、多态
class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print("汽车启动")
car=Car("宝马")
car.start()
print(car.brand+"品牌")


