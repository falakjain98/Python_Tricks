#! python3
# volume.py - exploring some UDF tricks in python

# Nesting a function with a parent function (closure function)
def get_speak_func(text,volume):
    def whisper():
        return text.lower()+'...'
    def yell():
        return text.upper()+'!!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func('Hello World',0.7)())

# Objects behaving as functions
class Adder:
    def __init__(self,n):
        self.n = n

    def __call__(self,x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))

'''
Everything in Python is an object!!
'''