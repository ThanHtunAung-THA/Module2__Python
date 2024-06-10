#8_raising_exception.py

try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    if b == 0:
        raise ZeroDivisionError
    else:
        print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero!")
except ValueError:
    print("please use a and b as integer value!")
