t1 = input()
t2 = input()

t1_int = ''
t2_int = ''

for c in t1:
    if c.isdigit():
        t1_int += c

for c in t2:
    if c.isdigit():
        t2_int += c

print(int(t1_int) + int(t2_int))