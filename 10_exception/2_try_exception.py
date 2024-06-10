#10_exception
#2_try_exception.py

try:
    a = int(input('enter a : '))
    b = int(input('enter b : '))

    c = a/b

    print("a/b = ", c)
except Exception:
    print("can't divide by zero")
