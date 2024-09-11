n = int(input())

for i in range(1, 5000):
    n = n // i

    if n <= 1:
        print(i)
        break