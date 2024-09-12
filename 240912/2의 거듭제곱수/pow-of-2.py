N = int(input())

p = 0

while(True):
    if 2 ** p == N:
        break
    p += 1

print(p)