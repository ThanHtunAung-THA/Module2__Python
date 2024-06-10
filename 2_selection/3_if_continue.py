age = int(input("how old are you !"))

if age >85 and age <= 100:
    print("very old")
if age >60 and age <= 85:
    print("Old")
if age >40 and age <= 60:
    print("very adult")
if age >30 and age <= 40:
    print("adult")
if age >20 and age <= 30:
    print("young")
if age >10 and age <= 20:
    print("teenager")
if age >=1 and age <= 10:
    print("baby")
if age >100 or age <1:
    print("invalid age !")
