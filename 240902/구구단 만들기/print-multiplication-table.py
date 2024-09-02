a, b = map(int, input().split())

dan = []

for i in range(b, a - 1, -1):
    if i % 2 == 0:
        dan.append(i)

for i in range(1, 10):
    result = []

    for d in dan:
        result.append("{d} * {i} = {res}".format(d=d, i=i, res=d*i))
    
    print(" / ".join(result))