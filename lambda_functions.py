#! oython3
# lambda.py - exploring the functionality of lambda functions

# lambda can be used to declare small anonymous functions and have implicit returns
add = lambda x,y: x + y
print(add(5,3))

# calling lambda function without assigning a function name
print((lambda x,y: x + y)(5,3))

# lambda function to sort tuple by computed key
tuples = [(1,'d'),(2,'b'),(4,'a'),(3,'c')]
print(sorted(tuples,key = lambda x: x[1]))

# lambda function to sort ranges by a computed key
print(sorted(range(-5,6), key = lambda x:x*x))

# lambda functions as lexical closures (remembers values from the enclosing scope)
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))

# lambda functions might be fancy to view and implement but they 
# can lead to incomprehensible code if viewed by someone else
# therefore use lambda functions judiciously