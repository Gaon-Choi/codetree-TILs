n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_partial_series = False

for i in range(n1 - n2 + 1):
    if A[i:i + n2] == B:
        is_partial_series = True
        break

if is_partial_series:
    print("Yes")
else:
    print("No")