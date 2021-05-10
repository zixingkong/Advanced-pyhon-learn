# 实现多线程编程的
# 方法1：实例化Thread类

import threading
import time


def get_html_detail():
	print("get url detail start")
	time.sleep(2)
	print("get url detail end")


def get_url_list():
	print("get url list start")
	time.sleep(2)
	print("get url list end")


# 2. 继承Thread类
class GetHtmlDetail(threading.Thread):
	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print("get url detail start")
		time.sleep(2)
		print("get url detail end")


class GetUrlList(threading.Thread):
	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print("get url list start")
		time.sleep(2)
		print("get url list end")


if __name__ == "__main__":
	start_time = time.time()
	# thread1 = threading.Thread(target=get_html_detail)
	# thread2 = threading.Thread(target=get_url_list)
	# thread1.setDaemon(True)
	# thread2.setDaemon(True)

	thread1 = GetHtmlDetail("get_html_detail")
	thread2 = GetUrlList("get_url_list")
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print("last time {}".format(time.time() - start_time))
