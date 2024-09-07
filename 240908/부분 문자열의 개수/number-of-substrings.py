A = input()
B = input()

cnt = 0

for i in range(len(A)):
    if i + len(B) - 1 < len(A):
        if A[i:i+len(B)] == B:
            cnt += 1

print(cnt)