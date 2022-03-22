# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     thread_communication
   Description :
   date：          2022/3/21
-------------------------------------------------
"""

detail_url_list = []

import time
import threading


detail_url_list = []


def get_datail_html():
    # 爬取文章详情页
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))

        print("get detail url end")


if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list))
    for i in range(10):
        html_thread = threading.Thread(target=get_datail_html, args=(detail_url_list))
        html_thread.start()
    start_time = time.time()
    print("last time:{}".format(time.time() - start_time))