is_composite = False

n = int(input())

for i in range(2, n):
    if n % i == 0:
        is_composite = True
        break

print("C" if is_composite else "N")