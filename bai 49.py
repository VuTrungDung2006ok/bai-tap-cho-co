n = input()
a = []
d = ''
for i in n:
    if i.isdigit():
        d += i
    elif d:
        a.append(int(d))
        d = ''

print(d)






