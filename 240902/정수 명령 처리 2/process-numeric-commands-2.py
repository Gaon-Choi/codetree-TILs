queue = []

N = int(input())

for _ in range(N):
    query = input().split()
    if query[0] == "push":
        queue.append(int(query[1]))
    elif query[0] == "front":
        print(queue[0])
    elif query[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif query[0] == "size":
        print(len(queue))
    elif query[0] == "pop":
        print(queue[0])
        queue.pop(0)