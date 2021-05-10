# 实现多线程编程的方法1：实例化Thread类

import threading
import time


def get_html_detail():
    print("get url detail start",end='\n')
    time.sleep(2)
    print("get url detail end",end='\n')


def get_url_list():
    print("get url list start",end='\n')
    time.sleep(2)
    print("get url list end",end='\n')


if __name__ == "__main__":
    start_time = time.time()
    thread1 = threading.Thread(target=get_html_detail)
    thread2 = threading.Thread(target=get_url_list)
    thread1.start()
    thread2.start()
    
    print("last time {}".format(time.time()-start_time))