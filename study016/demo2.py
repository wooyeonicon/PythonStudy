# 作者 : 杨航
# 开发时间 : 2022/7/21 11:52
# 在导入带有包的模块时注意事项
import package1
# 使用import方式进行导入时，只能跟 包名 或 模块名
from package1 import module_A
from package1.module_A import a
# 使用from...import可以导入包、模块、函数、变量