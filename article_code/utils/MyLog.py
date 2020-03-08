import sys
import inspect


def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]


def fun_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3] + ':'


def my_code_name():
    return __name__ + sys._getframe().f_code.co_name


def my_print(*args, sep=' ', end='\n', file=None):
    # name = sys._getframe().f_code.co_name
    if True:
        print(*args, sep=' ', end='\n', file=None)


if __name__ == '__main__':
    my_print(my_code_name(), 'sfsfaf' + 'adsfs')
    # MyLog.my_print(self.__class__.__name__, MyLog.fun_name(), love)

