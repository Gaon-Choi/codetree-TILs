a, b = map(int, input().split())

if a > b:
    a, b = b, a

result = 0

for elem in range(a, b + 1):
    if elem % 5 == 0:
        result += elem

print(result)