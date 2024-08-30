def is_369(num):
    if '3' in str(num):
        return True
    elif '6' in str(num):
        return True
    elif '9' in str(num):
        return True
    elif num % 3 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())

count = 0

for i in range(a, b + 1):
    if is_369(i):
        count += 1

print(count)