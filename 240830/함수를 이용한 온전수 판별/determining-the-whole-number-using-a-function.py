def is_complete_number(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True

a, b = map(int, input().split())

count = 0

for num in range(a, b+1):
    if is_complete_number(num):
        count += 1

print(count)