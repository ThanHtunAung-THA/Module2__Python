#14_variable_lenght_args.py
def signup_member(**kwargs):
    for i,a in kwargs.items():
        print(f"{i}=>{a}")
        
signup_member(name="kyawkyaw", age="25", gender="male")
