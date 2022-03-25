# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sync_read_yaml
   Description :
   date：          2022/3/24
-------------------------------------------------
"""
import asyncio
import os
import time
import aiofiles


def yaml_load(dir='/Users/wyy/code/github/python/Advanced-pyhon-learn/learn/testcase', file=''):
    """
    异步读取yaml文件，并转义其中的特殊值
    :param file:
    :return:
    """
    if dir:
        file = os.path.join(dir, file)
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()

    # data = yaml.load(data)
    print(data)
    print('-' * 80)
    return data


if __name__ == '__main__':
    start_time = time.time()
    project_dir = os.path.dirname(os.path.dirname(__file__))
    test_case_dir = os.path.join(project_dir, "testcase")
    case_list = os.listdir(test_case_dir)
    for case in case_list:
        yaml_load(file=case)
    print(time.time() - start_time)
