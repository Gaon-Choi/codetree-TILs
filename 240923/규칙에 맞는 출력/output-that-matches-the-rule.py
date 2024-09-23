N = int(input())

for i in range(N):
    arr = list(range(N-i, N + 1))
    for elem in arr:
        print(elem, end=" ")
    print()