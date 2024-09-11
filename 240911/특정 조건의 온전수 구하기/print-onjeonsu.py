def is_complete_number(n: int):
    if (n % 2 != 0 and n % 10 != 5 and not (n % 3 == 0 and n % 9 != 0)):
        return True
    return False

N = int(input())

for n in range(1, N + 1):
    if is_complete_number(n):
        print(n, end=" ")