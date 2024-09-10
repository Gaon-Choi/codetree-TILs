t1, t2 = input().split()

t1_int = ''
t2_int = ''

for c in t1:
    if c.isdigit():
        t1_int += c
    else:
        break

for c in t2:
    if c.isdigit():
        t2_int += c
    else:
        break

print(int(t1_int) + int(t2_int))