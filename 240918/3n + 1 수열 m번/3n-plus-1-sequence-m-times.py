def calculate_when_becomes_1(num: int):
    temp = num
    count = 0
    while (temp != 1):
        count += 1
        if temp % 2 == 0:
            temp = temp // 2
        else:
            temp = 3 * temp + 1
    return count

n = int(input())

for _ in range(n):
    number = int(input())
    print(calculate_when_becomes_1(number))