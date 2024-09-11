N = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i, N):
        #print(i, j)
        total_sum = float(sum(arr[i:j+1]) / len(arr[i:j+1]))
        if total_sum in arr[i:j+1]:
            #print(total_sum, arr[i:j+1])
            cnt += 1



print(cnt)