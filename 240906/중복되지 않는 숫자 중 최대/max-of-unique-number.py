N = int(input())
arr = list(map(int, input().split()))

tmp = []

for elem in arr:
    if arr.count(elem) == 1:
        tmp.append(elem)

if not tmp:
    print(-1)
else:
    print(max(tmp))