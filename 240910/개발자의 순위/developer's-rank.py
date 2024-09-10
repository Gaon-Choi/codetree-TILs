# K : 경기의 횟수
# N : 개발자의 수

K, N = map(int, input().split())

arr = []

for _ in range(K):
    arr.append(list(map(int, input().split())))

result = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            flag = True
            for k in range(K):
                if arr[k].index(j) > arr[k].index(i):
                    flag = False
                    break
            if flag:
                result += 1

print(result)