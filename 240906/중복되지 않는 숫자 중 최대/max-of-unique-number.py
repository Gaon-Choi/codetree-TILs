N = int(input())
arr = list(map(int, input().split()))

tmp = []

for elem in arr:
    if elem in tmp:
        tmp.remove(elem)
    else:
        tmp.append(elem)

if not tmp:
    print(-1)
else:
    print(max(tmp))