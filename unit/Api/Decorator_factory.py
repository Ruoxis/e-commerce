
class MyDecorator:
    def __init__(self, *args_1, **kwargs_1):
        """
        装饰可以自定义前置执行模块与后置执行模块
        {before_func = 前置执行方法,after_func = 后置执行方法}
        :param args_1:
        :param kwargs_1:
        """
        self.before_func = kwargs_1.pop('before_func', None)
        self.after_func = kwargs_1.pop('after_func', None)
        self.arg_1 = args_1
        self.kwarg_2 = kwargs_1

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 在调用被装饰的函数之前执行的操作
            if self.before_func:
                self.before_func()
            print(f"装饰器3参数: {self.arg_1}, {self.kwarg_2}")
            # 调用被装饰的函数
            result = func(*args, **kwargs)

            # 在调用被装饰的函数之后执行的操作
            if self.after_func:
                self.after_func()

            return result

        return wrapper


if __name__ == '__main__':
    """
    def my_before_call():
        print("在执行自身之前的操作")

    def my_after_call():
        print("在执行自身之后的操作")

    @MyDecorator("参数A", "参数B", before_func=my_before_call, after_func=my_after_call)
    def my_function():
        print("执行自身")

    # 使用装饰器调用被装饰的函数
    my_function()
    """
