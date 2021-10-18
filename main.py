# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'
import platform
import time

CURRENT_OS = platform.system()

if CURRENT_OS == 'Windows':
    from windows import EasyClicker

elif CURRENT_OS == 'Linux':
    from linux import EasyClicker


if __name__ == '__main__':
    if CURRENT_OS == 'Windows':
        print('Windows OS detected')
    elif CURRENT_OS == 'Linux':
        print('Lunux OS choiced')

    ec = EasyClicker()
    ec.run()
