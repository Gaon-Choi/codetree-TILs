def process(a, b):
    if a > b:
        return (a + 25, 2 * b)
    else:
        return (2 * a, b + 25)

a, b = map(int, input().split())

a, b = process(a, b)

print(a, b)