M, D = map(int, input().split())

a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if M <= 0 or M >= 12:
    print("Yes")
else:
    if a[M] < D:
        print("No")
    else:
        print("Yes")