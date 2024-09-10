def is_beautiful_array(a: list, b: list):
    if sorted(a) == b:
        return True
    else:
        return False

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(len(A) - len(B) + 1):
    if is_beautiful_array(A[i:i+len(B)], B):
        cnt += 1

print(cnt)