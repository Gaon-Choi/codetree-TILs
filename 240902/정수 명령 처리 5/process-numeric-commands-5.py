N = int(input())

result = []

for _ in range(N):
    query = input().split()

    if query[0] == "push_back":
        result.append(int(query[1]))
    elif query[0] == "get":
        print(result[int(query[1]) - 1])
    elif query[0] == "size":
        print(len(result))
    elif query[0] == "pop_back":
        result.pop()