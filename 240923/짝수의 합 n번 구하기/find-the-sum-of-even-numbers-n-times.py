def sum_up_even(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num

    return total

N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    print(sum_up_even(start, end))