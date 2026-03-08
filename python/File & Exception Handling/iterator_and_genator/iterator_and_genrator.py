# today's agenda -
# iterator - it controls the flow of iterable elements
# genrator - 

# revision - exception handling

# 3 types of error -
# syntax error
# logical error
# runtime error

# all about error - which errror comes for what reasons  - most common
# return only extract single value allways
# every function/method has a return type it depends on the value we pass in it
# yield is not a last keyword in your generator 

# ----------------------------------------------------------------

# iterable -

# ----------------------------------------------------------------
# ex -

l1 = [10, 20, 30]
# for i in l1:
#     print(i)
# break  # break is used to stop the loop

# ----------------------------------------------------------------

l1 = iter(l1)  # iterator - a func that returns an iterator
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))

i2 = l1.__iter__()  # iterator
# print(next(i2))
# ----------------------------------------------------------------


def number(num1):
    for i in range(0, num1):
        # print(i)
        return i


# print(type(number(10)))  # <class 'int'>


def number(name):
    return name


# print(type(number('kartik')))  # <class 'str'>


def number():
    pass


# print(type(number()))  # <class 'NoneType'>

def number1():
    yield 1
    yield 2

print(list(number1()))  # <generator object number1 at 0x000001E6B5C6F0F0>

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

# timeframe - 32:00
