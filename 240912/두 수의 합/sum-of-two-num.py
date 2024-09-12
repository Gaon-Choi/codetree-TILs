n, k = map(int, input().split())
arr = list(map(int, input().split()))

hashMap = dict()

for elem in arr:
    if elem in hashMap:
        hashMap[elem] += 1
    else:
        hashMap[elem] = 1

arr = list(set(arr))

result = 0

for elem in arr:
    complement = k - elem
    if complement in hashMap:
        result += hashMap[complement]
    #result += hashMap[complement] * hashMap[elem]

print(result // 2)