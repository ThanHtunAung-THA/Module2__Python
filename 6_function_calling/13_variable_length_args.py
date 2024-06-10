#13_variable_length_args.py
def show_member(*names):
    for i in names:
        print(i)
        
show_member("kyawkyaw", "aungaung", "ayeaye", "susu")
