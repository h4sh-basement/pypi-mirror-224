# -*- coding: utf-8 -*-
"""
定义一些函数装饰器
"""
import inspect
import time


def show_running_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        running_time = end_time - start_time
        print(f'{func} running time f= {running_time} s.')
        return result

    return wrapper


def trace_calls(func):
    def wrapper(*args, **kwargs):
        call_stack = inspect.stack()
        call_frames = []
        for frame in call_stack[1:]:
            filename = frame.filename.split('src')[-1]
            call_frames.append((filename, frame.function, frame.lineno))
        print(f'{func} called from:')
        for frame in call_frames:
            print(f'\t{frame[0]}:{frame[1]}: line {frame[2]}')
        return func(*args, **kwargs)

    return wrapper
