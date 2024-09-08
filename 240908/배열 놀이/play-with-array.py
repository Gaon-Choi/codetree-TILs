n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        print(arr[query[1] - 1])

    elif query[0] == 2:
        search = query[1]

        if search in arr:
            print(arr.index(search) + 1)
        else:
            print(0)

    elif query[0] == 3:
        for elem in arr[query[1]-1:query[2]]:
            print(elem, end=" ")
        
        print()