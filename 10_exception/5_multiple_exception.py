#10_exception
#5_try_exception.py

try:
    a = int(input('enter a : '))
    b = int(input('enter b : '))

    c = a/b

    print("a/b = ", c)
except (ZeroDivisionError, ValueError):
    print("can't divide by zero")
else:
    print('else block call')
