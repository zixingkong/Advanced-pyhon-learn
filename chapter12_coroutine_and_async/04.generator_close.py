# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/14 上午10:30
# @Author  : QA-wyy
# @File    : 04.generator_close.py
# @Description: 
-------------------------------------------------
"""


def gen_func():
	# 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
	try:
		yield "http://projectsedu.com"
	except BaseException:
		pass
	yield 2
	yield 3
	return "bobby"


if __name__ == "__main__":
	gen = gen_func()
	print(next(gen))
	gen.close()
	print("bobby")

# GeneratorExit是继承自BaseException， Exception
