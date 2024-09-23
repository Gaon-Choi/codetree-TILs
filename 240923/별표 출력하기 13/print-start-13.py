n = int(input())

even = n
odd = 1

arr = []

for i in range(n):
    if i % 2 == 0:
        arr.append(even)
        even -= 1
    else:
        arr.append(odd)
        odd += 1

for elem in arr:
    print("* " * elem)

# 상하 대칭    
arr.reverse()

for elem in arr:
    print("* " * elem)