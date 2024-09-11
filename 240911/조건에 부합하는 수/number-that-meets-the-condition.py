a = int(input())

for n in range(1, a + 1):
    A = (n % 2 == 0) and (n % 4 != 0)
    B = (n // 8) % 2 == 0
    C = n % 7 < 4

    if not A and not B and not C:
        print(n, end=" ")