N = int(input())

pascal = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j or j == 0:
            pascal[i][j] = 1

for i in range(N):
    for j in range(i):
        if i != j and j != 0:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for i in range(N):
    for j in range(N):
        if pascal[i][j] > 0:
            print(pascal[i][j], end=" ")
        
    print()