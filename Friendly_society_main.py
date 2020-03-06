
from Friendly_Society.Friendly_society import *
import threading

# 一次进入友爱社人员数量
num = 5

# 获得cookie合集
from Friendly_Society.Friendly_society import Friendly_society


def get_Cookie():
    Cookie_list = []
    with open('cookies.txt', 'r+') as f:
        for ck in f:
            Cookie_list.append(ck.strip())
    return Cookie_list


# 多线程运行开启
def thread_function(target):
    cookies = get_Cookie()
    ck_len = len(cookies)
    start = 0
    stop = num
    while True:
        threadpool = []
        print('本次获取范围为%d-%d' % (start, stop - 1))
        for i in range(start, stop):
            cookie = cookies[i]
            task = threading.Thread(target=target, args=(cookie,))
            threadpool.append(task)
        for t in threadpool:
            t.start()
        for t in threadpool:
            t.join()
        start = stop
        stop += num
        if start == ck_len:
            print('没账号了~退出')
            break
        if stop > ck_len:
            stop = ck_len


def sum_requests(cookie):
    try:
        temp = Friendly_society(cookie)
        # 申请加入
        temp.doSign()
        temp.Join_friendly_society()
        #设置休眠 确保所有账户都已经进入了友爱社  看实际网络情况进行延迟
        time.sleep(35)
        # 开始批量心跳
        temp.Pc_AppHearbeat()
        time.sleep(300)
        temp.Pc_AppHearbeat()
        # 开始批量领取双端奖励
        temp.receive_award()
        # 退出
        temp.quit()
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(2)
        sum_requests(cookie)
# threadmax.release()


# 运行核心
def run():
    start = time.time()
    thread_function(sum_requests)
    print(f"请求用时{time.time() - start}")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)
