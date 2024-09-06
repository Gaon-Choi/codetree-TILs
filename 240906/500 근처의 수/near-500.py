arr = list(map(int, input().split()))

under_500 = list(filter(lambda x : x < 500, arr))
above_500 = list(filter(lambda x : x > 500, arr))

print(max(under_500), min(above_500))