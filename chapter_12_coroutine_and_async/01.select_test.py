# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/14 上午10:02
# @Author  : QA-wyy
# @File    : 01.select_test.py
# @Description: 
-------------------------------------------------
"""
# 并发 并行
# 并发：指一个时间段内，有几个程序在同一个CPU上运行，但是任意时刻只有一个程序在CPU上运行
# 并行：任意时刻点上，有多个程序同时运行在多个CPU上

# 同步 异步 （消息之间的通信机制）
# 同步：代码调用IO操作时，必须等待IO操作完成才返回的调用方式
# 异步：代码调用IO操作时，不必等IO操作完成就返回的调用方式

# 阻塞 非阻塞 （函数调用的机制）
# 阻塞：调用函数时当前线程被挂起
# 非阻塞：调用函数时当前线程不会挂起，而是立即返回

# C10K 问题：
# UNIX 五种I/O模型
# 1、阻塞式I/O
# 2、非阻塞式I/O
# 3、I/O复用
# 	select： 可以监听多个socket的状态
# 	poll：
# 	epoll：
# 4、信号驱动式I/O
# 5、异步I/O（POSIX的aio系列函数）


# 1. epoll并不代表一定比select好
# 网站：在并发高的情况下，连接活跃度不是很高， epoll比select好
# 游戏：并发性不高，同时连接很活跃， select比epoll好

# 通过非阻塞io实现http请求

import socket
from urllib.parse import urlparse


# 使用非阻塞io完成http请求

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好， 需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    get_url("https://www.baidu.com")
