n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

money = k
result = 0

for elem in coins:
    result += money // elem
    money = money % elem

print(result)