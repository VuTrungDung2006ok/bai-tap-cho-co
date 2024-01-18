a = input()
b = input()
d = ''
for i in a:
    d += i
for i in b:
    d += i

e = ''.join(sorted(set(d), key=d.index))
print(e)







