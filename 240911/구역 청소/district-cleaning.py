a, b = map(int, input().split())
c, d = map(int, input().split())

# 두 영역이 겹치지 않는 경우
if b < c or d < a:
    print((b-a) + (d-c))
# 두 영역이 겹치는 범위가 있는 경우
else:
    # b > c and d > a
    print(max(a, b, c, d) - min(a, b, c, d))