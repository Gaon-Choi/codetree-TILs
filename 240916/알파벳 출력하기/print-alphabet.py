n = int(input())

num = ord("A")

for i in range(n):
    for j in range(i + 1):
        print(chr(num), end="")
        if num == ord("Z"):
            num = ord("A")
            continue
        num += 1
    print()