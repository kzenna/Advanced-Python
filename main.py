# Домашнее задание к лекции
# ««Decorators»»
#
# Кокурникова Лилия Фаритовна, 02.05.19
#
import time
import datetime
import logging


def my_log(func):
    def wrapper(self, *argv, **kwargv):
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(func.__doc__)
        return func(self, *argv, **kwargv)
    return wrapper


def func_detail(func):
    def func_wrapper(*args, **kwargs):
        print(time.time())
        print(datetime.datetime.now())
        print(func.__name__)
        print(*args)
        print(kwargs)
        return func(*args, **kwargs)
    return func_wrapper


if __name__ == '__main__':
    n = 2
    @my_log
    @func_detail
    def my_function(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return my_function(n - 1) + my_function(n - 2)