# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rename
   Description :
   date：          2022/2/19
-------------------------------------------------
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

file_lst = []
for fpathe, dirs, fs in os.walk('/Users/wyy/code/github/python/Fluent-Python'):
    for f in fs:
        if f.endswith('.py'):
            # print(os.path.join(fpathe, f))
            file_lst.append(os.path.join(fpathe, f))



for fileAbstractPath in file_lst:
    directory = os.path.dirname(fileAbstractPath)
    file_name = os.path.split(fileAbstractPath)[-1]

    if file_name.count('.') == 2:
        new_name = file_name.replace('.', '_',1)
        oldname = directory + os.sep + file_name  # os.sep添加系统分隔符

        # 设置新文件名
        newname = directory + os.sep +  new_name
        print(oldname,'->',newname)
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    else:
        continue

