#21_list_filter_args.py

L= {1,2,3,4,10,123,22}

new_list= list(filter(lambda x : (x%3 == 0), L))

print(new_list)
