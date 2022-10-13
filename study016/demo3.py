# 作者 : 杨航
# 开发时间 : 2022/7/21 11:57

import sys
import time
import urllib.request
import math
import decimal

# 查看字节
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

# 查看时间
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())

# 数学
print(math.pi)

# 精度
