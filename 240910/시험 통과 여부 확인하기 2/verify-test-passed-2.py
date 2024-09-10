n = int(input())

result = 0

for _ in range(n):
    if sum(list(map(int, input().split()))) >= 240:
        print("pass")
        result += 1
    else:
        print("fail")

print(result)