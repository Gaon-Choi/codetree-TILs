# 직사각형의 겹침

# 선분의 겹침 조건은 2가지였음
# 이것이 x, y축으로 각각 확장된다고 보면 됨

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x2 < a1 or a2 < x1 or b2 < y1 or y2 < b1:
    print("nonoverlapping")
else:
    print("overlapping")