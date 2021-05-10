# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/10 上午10:11
# @Author  : QA-wyy
# @File    : 03.thread_safe_queue.py
# @Description: 
-------------------------------------------------
"""

from threading import Thread
from queue import Queue
import time


def get_html_detail(queue):
	queue.get()
	print("get url detail start")
	time.sleep(2)
	print("get url detail end")


def get_url_list(queue):
	for i in range(10):
		queue.put("http://{}".format(i))
		print("get url list start")
		time.sleep(2)
		print("get url list end")


if __name__ == "__main__":
	queue = Queue(maxsize=20)
	start_time = time.time()
	thread1 = Thread(target=get_url_list, args=(queue,))
	thread1.start()
	for i in range(10):
		thread2 = Thread(target=get_html_detail, args=(queue,))
		thread2.start()

	print("last time {}".format(time.time() - start_time))
