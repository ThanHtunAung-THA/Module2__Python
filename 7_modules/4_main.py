#4_main.py

def sum(a,b):
    return a+b

def multiple(a,b):
    return a*b

def remainder(a,b):
    return a%b

try:
    from Calculator import remainder as re
except ImportError:
    print('error')
    def re(a,b):
        return a % b

a=int(input('enter a: '))
b=int(input('enter b: '))

print("result =", re(a,b))
