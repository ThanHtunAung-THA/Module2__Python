age = int(input("how old are you !"))

if age >85 and age <= 100:
    print("very old")
elif age >60 and age <= 85:
    print("Old")
elif age >40 and age <= 60:
    print("very adult")
elif age >30 and age <= 40:
    print("adult")
elif age >20 and age <= 30:
    print("young")
elif age >10 and age <= 20:
    print("teenager")
elif age >=1 and age <= 10:
    print("baby")
else:
    print("invalid age !")