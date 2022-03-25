# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     find_case
   Description :
   date：          2022/1/27
-------------------------------------------------
"""


class A():

    @classmethod
    def getTestMethods(self):
        """
        Methods starts with "test" will be executed aotumatically,
        And will be uploaded as a case. Task will be consider as success only if all the cases
        """
        test_methods = list(filter(lambda x: x.startswith('test') and callable(getattr(self, x)), dir(self)))

        return test_methods

    def test_1(self):
        print("test1")

    def test_2(self):
        print('test2')

    def test_3(self):
        print('test3')


if __name__ == '__main__':
    import importlib

    my_module = importlib.import_module('find_case')
    MyClass = getattr(my_module, 'A')
    test_case = MyClass.getTestMethods()
    print(test_case)
    # print(dir(MyClass))
    # print(test_case)
