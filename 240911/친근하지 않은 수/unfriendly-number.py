def is_familiar_number(n: int):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

N = int(input())

count = 0

for n in range(1, N + 1):
    if not is_familiar_number(n):
        count += 1

print(count)