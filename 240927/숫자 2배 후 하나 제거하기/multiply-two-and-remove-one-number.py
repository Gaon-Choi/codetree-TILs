import copy

n = int(input())

arr = list(map(int, input().split()))
temp = []

for i in range(n):
    for j in range(n):
        diffsum = 0

        temp_arr = copy.deepcopy(arr)

        temp_arr[i] *= 2

        temp_arr.pop(j)

        for i in range(len(temp_arr) - 1):
            diffsum += abs(temp_arr[i] - temp_arr[i+1])

        
        temp.append(diffsum)

print(min(temp))