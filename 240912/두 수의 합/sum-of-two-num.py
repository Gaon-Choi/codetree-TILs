n, k = map(int, input().split())

hashMap = dict()

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) in hashMap:
            hashMap[arr[i] + arr[j]] += 1
        else:
            hashMap[arr[i] + arr[j]] = 1

print(hashMap[k])