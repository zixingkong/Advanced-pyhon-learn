# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/14 上午10:31
# @Author  : QA-wyy
# @File    : 05.generator_throw.py
# @Description: 
-------------------------------------------------
"""


def gen_func():
    # 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
    try:
        yield "http://projectsedu.com"
    except Exception as e:
        pass

    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")
