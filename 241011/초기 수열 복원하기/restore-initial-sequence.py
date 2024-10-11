def is_valid_arr(arr: list, n: int):
    is_unique = len(arr) == len(set(arr))

    is_all_range = True
    for elem in arr:
        if not (1 <= elem and elem <= n):
            is_all_range = False
            break
    
    return is_unique and is_all_range


N = int(input())

arr = list(map(int, input().split()))

answer = []


temp = []
for i in range(1, N+1):
    temp.append(i)

    for elem in arr:
        temp.append(elem - temp[-1])

    if is_valid_arr(temp, N):
        for elem in temp:
            print(elem, end=" ")
    temp = []