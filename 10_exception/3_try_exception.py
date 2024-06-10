#10_exception
#3_try_exception.py

try:
    a = int(input('enter a : '))
    b = int(input('enter b : '))

    c = a/b

    print("a/b = ", c)
except Exception:
    print("can't divide by zero, \
          please use as greater than zero")
