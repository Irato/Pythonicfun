
def contains_zero_handler():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except ZeroDivisionError:
        #if insert 0 
        print("You cannot divide by zero, sorry.")
    except ValueError:
        #if insert a letter , float , etc...
        print("You must enter an integer value.")
    except:
        #if crtl+c throws keyboard interrupt exception
        print("Oh dear, something went wrong...")

    print("THE END.")

def not_contain_zero_handler():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except ValueError:
        #if insert a letter , float , etc...
        print("You must enter an integer value.")
    except:
        #if crtl+c throws keyboard interrupt exception
        print("Oh dear, something went wrong...")

    print("THE END.")


def no_handler():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except ValueError:
        #if insert a letter , float , etc...
        print("You must enter an integer value.")
    print("THE END.")

def error_hierarchy():
    try:
        y = 1 / 0
    except (ArithmeticError,ZeroDivisionError) as e:
        print(e)
        print("Oooppsss...")

    print("THE END.")

# def bad_fun(n):
#     raise ZeroDivisionError
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("What happened? An error?")

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("I did it again!")
#         #re reaise the same exception handled
#         raise
# try:
#     bad_fun(0)
# except ZeroDivisionError:
#     print("I see!")

# print("THE END.")

# The Python statement "assert" expression evaluates the expression and raises the AssertError 
# exception when the expression is equal to zero, an empty string, or None.
#  You can use it to protect some critical parts of your code from devastating data.


# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
#Exception when the number generated is to big
def exceptions_arit():
    from math import exp

    ex = 1

    try:
        while True:
            print(exp(ex))
            ex *= 2
    except OverflowError:
        print('The number is too big.')

# How to abuse the dictionary
# and how to deal with it?
def key_err_exception():
    dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
    ch = 'a'

    try:
        while True:
            ch = dictionary[ch]
            print(ch)
    except KeyError:
        print('No such key:', ch)

key_err_exception()