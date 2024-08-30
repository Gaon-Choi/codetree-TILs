n = int(input())

count = 1
for _ in range(n):
    for _ in range(n):
        print(str(count % 10) + " ", end="")
        count += 1
        if count % 10 == 0:
            count += 1

    print()