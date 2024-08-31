n = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        num_list[i] = num_list[i] // 2

for elem in num_list:
    print(elem, " ", sep="", end="")