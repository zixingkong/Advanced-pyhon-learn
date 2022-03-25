# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yield_from_example
   Description :   学习 yield from
   date：          2022/3/22
-------------------------------------------------
"""

final_result = {}


def sum(pro_name):
    total = 0
    num = []
    while True:
        x = yield
        print(pro_name + '销量：', x)
        if not x:
            break
        total += x
        num.append(x)
    return total, num


def middle(key):
    # 为什么添加这句就不报StopIteration异常了？
    while True:
        final_result[key] = yield from sum(key)
        print(key + '统计完成 ！！！')


def main():
    data_sets = {
        "bobby牌面膜": [1200, 1500, 3000],
        "bobby牌手机": [28, 55, 98, 108],
        "bobby牌大衣": [280, 560, 778, 70],
    }

    for key, values in data_sets.items():
        print("start key:", key)
        mid = middle(key)
        mid.send(None)
        for value in values:
            mid.send(value)
        mid.send(None)

    print('final result:', final_result)


if __name__ == '__main__':
    main()
