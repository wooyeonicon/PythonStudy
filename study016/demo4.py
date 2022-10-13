# 作者 : 杨航
# 开发时间 : 2022/7/21 12:11
# 每隔一段时间，发送一条任务（可以做定时任务）
import time

import schedule
def job():
    print("哈哈---")

schedule.every(3).seconds.do(job)  # 每三秒执行一次job
while True:
    schedule.run_pending()  # 启动
    time.sleep(1)  # 每执行一次睡眠一秒