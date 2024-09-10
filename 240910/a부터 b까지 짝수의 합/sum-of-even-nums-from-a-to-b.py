a, b = map(int, input().split())

print(sum(list(filter(lambda x: x % 2 == 0, list(range(a, b + 1))))))