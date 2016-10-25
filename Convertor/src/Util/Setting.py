#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'guipengliang'

import sys
import os
import datetime
import time
import logging
#import logging.handlers

from Util.Singleton import *

LogPathName='./logs'

@singleton
class Settings(object):

    def __init__(self):
        # super(Settings, self).__init__()
        object.__init__(self)

        self.__initLog()
        pass

    def __del__(self):
        pass

    def __initLog(self):
        path=LogPathName
        if not os.path.exists(path):
            os.makedirs(path)

        #logFileName=time.strftime('%Y-%m-%d %H.%M.%S',time.localtime())+'.log'
        logFileName=time.strftime('%Y-%m-%d',time.localtime())+'.log'
        LOG_FILE = os.path.join(path,logFileName)

        logging.basicConfig(filename = LOG_FILE, filemode = 'a', level = logging.DEBUG, format = '%(asctime)s [%(levelname)s] %(message)s -- in the %(funcName)s function of %(pathname)s:%(lineno)s - %(name)s')

        # handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
        # fmt = '%(asctime)s [%(levelname)s] %(message)s -- in the %(funcName)s function of %(pathname)s:%(lineno)s - %(name)s'
        #
        # formatter = logging.Formatter(fmt)   # 实例化formatter
        # handler.setFormatter(formatter)      # 为handler添加formatter
        #
        # self.__logger = logging.getLogger('tst')    # 获取名为tst的logger
        # self.__logger.addHandler(handler)           # 为logger添加handler
        # self.__logger.setLevel(logging.DEBUG)

        # logger.info('first info message')
        # logger.debug('first debug message')


if __name__ == '__main__':
    test = Setting()
    pass
