from datetime import datetime
from typing import Callable
import numpy


def func_runtime(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        something = func(*args, **kwargs)
        finish_time = datetime.now() - start_time
        print(finish_time)
        return something
    return wrapper


@func_runtime
def get_normal_time(input: int | float) -> str:
    input = int(input)
    seconds = input % 60
    minutes = input // 60
    hours = minutes // 60
    minutes = minutes % 60

    return f'{hours}:{minutes}:{seconds}'


@func_runtime
def get_normal_time_another_int(input: int | float) -> str:
    input = input // 1
    seconds = input % 60
    minutes = input // 60
    hours = minutes // 60
    minutes = minutes % 60

    return f'{hours}:{minutes}:{seconds}'


@func_runtime
def get_normal_time_math(input: int | float) -> str:

    input = int(input)
    arr1 = [input]
    arr2 = [60]

    seconds = numpy.remainder(arr1, arr2)
    minutes = numpy.floor_divide(arr1, arr2)
    hours = numpy.floor_divide(minutes, arr2)
    minutes = numpy.remainder(minutes, arr2)

    return f'{hours[0]}:{minutes[0]}:{seconds[0]}'
