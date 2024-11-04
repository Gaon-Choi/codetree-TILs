A, B, x, y = map(int, input().split())

if (x > y):
    x, y = y, x

print(min(abs(B-A), abs(A-x)+abs(B-y)))