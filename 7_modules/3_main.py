#3_main.py
# from Calculator import *

# a= int(input("enter a: "))
# b= int(input("enter b: "))
# # a= input("enter a: ")
# # b= input("enter b: ")

# print("result = ", sum(a,b))

# from Calculator import *

# a = int(input("enter a: "))
# b = int(input("enter b: "))

# # Create a list containing a and b
# numbers = [a, b]

# # Use the built-in sum() function to sum the elements of the list
# print("result =", sum(numbers))

# =========================================================== #

def sum(a,b):
    return a+b

def multiple(a,b):
    return a*b

def remainder(a,b):
    return a%b

try:
    from Calculator import sum
except ImportError:
    print('error')

a=int(input('enter a: '))
b=int(input('enter b: '))

print("result2 =", sum(a,b))
