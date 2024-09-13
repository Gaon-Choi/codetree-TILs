n1 = 1920; n2 = 2880

a, b = map(int, input().split())

isExists = False

for i in range(a, b + 1):
    if n1 % i == 0 and n2 % i == 0:
        isExists = True
        break

print("1" if isExists else "0")