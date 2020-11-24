#!/usr/bin/env python

import time
import functools


def get_input(filename: str):
    with open(filename, "rt") as file_input:
        return file_input.read()


def timeit(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsed_time * 1000)))
        return result

    return wrap

