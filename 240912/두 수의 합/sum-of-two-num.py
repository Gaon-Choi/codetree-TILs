n, k = map(int, input().split())
arr = list(map(int, input().split()))

hashMap = dict()

for elem in arr:
    if elem in hashMap:
        hashMap[elem] += 1
    else:
        hashMap[elem] = 1





print(sum(hashMap.values()))