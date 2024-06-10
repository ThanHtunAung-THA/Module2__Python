#6_finally.py

try:
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    c = a/b

    print("a/b = ", c)

except ValueError:
    print('1')
except ValueError:
    print('1')
else:
    print('2')
finally:
    print('3')
