N = int(input())

arr = list(map(int, input().split()))

temp = []

for i in range(N):
    temp.append(arr.pop(0))
    
    if i % 2 == 0:
        temp.sort()
        print(temp[len(temp) // 2], end=" ")