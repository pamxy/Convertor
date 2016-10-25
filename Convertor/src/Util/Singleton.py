#encoding=utf-8
__author__ = 'guipengliang'

#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys


def singleton(cls,*args,**kw):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kw)
        return instances[cls]
    return _singleton


if __name__ == '__main__':
    @singleton
    class MyClass(object):
        a=1
        def __init__(self,x=0):
            self.x=x

    one=MyClass()
    two=MyClass()

    two.a=3
    print(one.a)
    pass












