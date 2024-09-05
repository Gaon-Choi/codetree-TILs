arr = list(map(int, input().split()))

cnt = 0
total = 0

for elem in arr:
    if elem == 0:
        break
    else:
        if elem % 2 == 0:
            cnt += 1
            total += elem

print(cnt, total)