#10_exception
#4_try_exception.py

try:
    a = int(input('enter a : '))
    b = int(input('enter b : '))

    c = a/b

    print("a/b = ", c)
except Exception:
    print("can't divide by zero")
else:
    print('else block call')
