print('True and False      =',True and False)
print('True or False       =',True or False)
print('not True            =',not True)
print('not not not True    =',not not not True)

name = "mgmg"
pw = 123

name1 = "koko"
pw1 = 123

name2 = "koko"
pw2 = 123

if(name1 == name and pw1 == pw or name1 == name2 and pw1 == pw2):
    print("login success")
else:
    print("something went wrong")
