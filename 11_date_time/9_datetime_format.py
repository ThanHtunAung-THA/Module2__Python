#9_datetime_format.py

from datetime import datetime

now = datetime.now()

print(now.strftime("%d"))
print(now.strftime("%a"))
print(now.strftime("%m"))
print(now.strftime("%B"))
print(now.strftime("%y"))
print(now.strftime("%Y"))
print(now.strftime("%a-%m-%Y"))
print(now.strftime("%d/%B/%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d/%B/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%Y %I:%M:%S"))


'''
01
Sat
06
June
24
2024
Sat-06-2024
01/June/2024
01/06/2024
01/June/2024 15:09:04
01/June/2024 03:09:04
'''
