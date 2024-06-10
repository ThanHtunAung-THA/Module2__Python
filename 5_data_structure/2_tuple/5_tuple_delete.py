t = (1,2,3,4,5)
print(t)

del t[0]
print(t)   #TypeError: 'tuple' object doesn't support item deletion

del t
print(t)  #error
