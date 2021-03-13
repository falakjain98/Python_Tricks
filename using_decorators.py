#! python3
# using_decorators.py - exploring the use of decorators in Python
# decorators can be effectively used for input/output logging

import functools

def null_decorator(func):
    return func

# @ syntax is a syntactic sugar
@null_decorator
def greet():
    return 'Hello!'

print(greet())

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

print(greet())

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper
def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

# Decorator stacking
@strong
@emphasis
def greet():
    return 'Hello!'

print(greet())

# Decorators which accept arguments
def proxy(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
            f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
            f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print(say('Jane','Hello, World'))



