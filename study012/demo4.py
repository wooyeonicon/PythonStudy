# 作者 : 杨航
# 开发时间 : 2022/4/12 11:53
# traceback
import traceback
try:
    print("====")
    print(1/0)
except:
    traceback.print_exc()