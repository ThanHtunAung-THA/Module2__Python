#16_set_intersection_update.py

s1 = set(['a', 'b', 'c','d'])
s2 = {'c','d', 'e', 'f'}

s1.intersection_update(s2)

print(s1)
print(s2)
