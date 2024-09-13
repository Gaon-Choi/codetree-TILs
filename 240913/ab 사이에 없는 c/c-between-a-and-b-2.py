a, b, c = map(int, input().split())

isExists = False

for i in range(a, b + 1):
    if c % i == 0:
        isExists = True
        break

print("YES" if isExists else "NO")