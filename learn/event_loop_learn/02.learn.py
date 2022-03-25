# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/20 22:04
# @Author  : ty
# @File    : 02.learn.py
# @Description: 
-------------------------------------------------
"""


def fun():
    print("step1")
    yield
    print("step2")
    yield
    print("step3")
    yield


scheduled_list = []


class Handle(object):
    def __init__(self, gen):
        self.gen = gen

    def call(self):
        next(self.gen)
        scheduled_list.append(self)


def loop(*coroutines):
    scheduled_list.extend(Handle(c) for c in coroutines)
    while True:
        while scheduled_list:
            handle = scheduled_list.pop(0)
            handle.call()


if __name__ == "__main__":
    loop(fun(), fun(), fun())
