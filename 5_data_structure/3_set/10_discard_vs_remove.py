#10_discard_vs_remove.py

s = {'a', 'b', 'c', 'd', 'd'}
print(s)


s.discard('A')
print(s)

s.remove('A')
print(s)
