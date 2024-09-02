dan = []
multiples = [2, 4, 6, 8]

a, b = map(int, input().split())

for i in range(a, b + 1):
    dan.append(i)

dan.sort(reverse=True)

for m in multiples:
    result = []
    for d in dan:
        result.append("{d} * {m} = {r}".format(d=d, m=m, r=d*m))

    print(" / ".join(result))