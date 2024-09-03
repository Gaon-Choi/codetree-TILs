n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

isSame = True

for i in range(n):
    if A[i] != B[i]:
        isSame = False
        break

if isSame:
    print("Yes")
else:
    print("No")