# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：资源检查
@File ：__init__.py.py
@Time ：2023/6/26 15:18
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""


# class Example:
#     @decorator_factory
#     def my_function(self, a='A', b='B'):
#         print("Inside decorator_factory {} {}".format(a, b))
#
#     @decorator_factory_("Hello, World!", 'sssss')
#     def my_function_(self, a='A', b='B'):
#         print("Inside decorator_factory_ {} {}".format(a, b))


# if __name__ == '__main__':
#     sss = Example()
#     sss.my_function()
#     print(123)
#     sss.my_function_()


def decorator1(func):
    print('装饰器1加载期间执行')

    def wrapper(self, *args, **kwargs):
        print("装饰器1执行前操作")
        result = func(self, *args, **kwargs)
        print("装饰器1执行后操作")
        return result

    return wrapper


def decorator2(func):
    print("装饰器2执行前操作")

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("装饰器2执行后操作")
        return result

    return wrapper


def decorator3(*arg1, **arg2):
    def decorator(func):
        print("装饰器3执行前操作")

        def wrapper(self, *args, **kwargs):
            print("装饰器3参数：{} {}".format(*arg1, **arg2))
            result = func(self, *args, **kwargs)
            print("装饰器3执行后操作")
            return result

        return wrapper

    return decorator


class MyClass:
    @decorator1
    def method1(self):
        print("方法1")

    @decorator2
    def method2(self):
        print("方法2")

    @decorator3("参数A", "参数B")
    def method3(self, a='AA', b='BB'):
        print("方法3")

    @decorator1
    @decorator2
    def method4(self):
        print("方法4")


# obj = MyClass()
# obj.method1()  # 装饰器1执行前操作 -> 方法1 -> 装饰器1执行后操作
# obj.method2()  # 装饰器2执行前操作 -> 方法2 -> 装饰器2执行后操作
# # obj.method3()
# # obj.method3()  # 装饰器1执行前操作 -> 装饰器2执行前操作 -> 方法3 -> 装饰器2执行后操作 -> 装饰器1执行后操作
# # @decorator3("参数C", "参数D")
# # # def method():
# # #     print("方法")
# # # method()
class MyDecorator:
    def __init__(self, before_func=None, after_func=None):
        self.before_func = before_func
        self.after_func = after_func

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 在调用被装饰的函数之前执行的操作
            if self.before_func:
                self.before_func()

            # 调用被装饰的函数
            result = func(*args, **kwargs)

            # 在调用被装饰的函数之后执行的操作
            if self.after_func:
                self.after_func()

            return result

        return wrapper

def my_before_call():
    print("在执行自身之前的操作")

def my_after_call():
    print("在执行自身之后的操作")

@MyDecorator(before_func=my_before_call, after_func=my_after_call)
def my_function():
    print("执行自身")

# 使用装饰器调用被装饰的函数
my_function()