n, A = input().split()
n = int(n)

result = 0

for _ in range(n):
    if A == input():
        result += 1

print(result)