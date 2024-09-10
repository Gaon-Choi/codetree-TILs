n = int(input())

arr = list(filter(lambda x: x % 2 == 0, list(map(int, input().split()))))[-1::-1]

for elem in arr:
    print(elem, end=" ")