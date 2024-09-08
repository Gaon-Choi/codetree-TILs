def is_369(n: int):
    if n % 3 == 0:
        return True
    else:
        if '3' in str(n) or '6' in str(n) or '9' in str(n):
            return True

    return False

n = int(input())

for i in range(1, n + 1):
    if is_369(i):
        print(0, end=" ")
    else:
        print(i, end=" ")