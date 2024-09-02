N = int(input())

hashmap = dict()

for _ in range(N):
    query = input().split()

    if query[0] == "add":
        hashmap[int(query[1])] = int(query[2])
    elif query[0] == "find":
        if int(query[1]) in hashmap:
            print(hashmap[int(query[1])])
        else:
            print("None")
    elif query[0] == "remove":
        if int(query[1]) in hashmap:
            hashmap.pop(int(query[1]))