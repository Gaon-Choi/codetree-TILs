A, B, C = map(int, input().split())

max_number = -1

a = C // A + 1
b = C // B + 1

for i in range(a):
    for j in range(b):
        temp = A * i + B * j
        if temp <= C:
            max_number = max(max_number, temp)

print(max_number)