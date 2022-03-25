# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     find_case
   Description :
   date：          2022/1/27
-------------------------------------------------
"""


def getTestMethods():
    """
    Methods starts with "test" will be executed aotumatically,
    And will be uploaded as a case. Task will be consider as success only if all the cases
    """
    print(dir())
    test_methods = list(filter(lambda x: x.startswith('test') and callable(x), dir()))

    return test_methods


def test_4():
    print("test4")


def test_5():
    print('test5')


if __name__ == '__main__':
    import importlib

    my_module = importlib.import_module('querytest')
    test_case = my_module.getTestMethods()
    print(test_case)
    # print(dir(MyClass))
    # print(test_case)
