#7_raising_exception.py

try:
    a = input("enter a: ")
    if not a.isnumeric():
        raise ValueError
    else:
        pass
except ValueError:
    print("please use a as integer value !")
