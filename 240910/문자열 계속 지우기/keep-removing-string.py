A = input()
B = input()

while(True):
    if B in A:
        idx = A.find(B)
        A = A[0:idx] + A[idx+len(B):]
    else:
        break

print(A)