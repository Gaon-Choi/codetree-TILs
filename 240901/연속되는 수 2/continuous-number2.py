prev = -1

N = int(input())

count = 0

for _ in range(N):
    a = int(input())

    if prev != a:
        count += 1

    prev = a

print(count)