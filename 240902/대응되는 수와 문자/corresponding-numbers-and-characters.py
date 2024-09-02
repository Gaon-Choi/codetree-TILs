n, m = map(int, input().split())

hashmap_1 = dict()
hashmap_2 = dict()

for i in range(n):
    word = input()
    hashmap_1[i + 1] = word
    hashmap_2[word] = i + 1

for i in range(m):
    q = input()
    if q.isdigit():
        print(hashmap_1[int(q)])
    else:
        print(hashmap_2[q])