x1, x2, x3, x4 = map(int, input().split())

# case 1
# x1---x2    x3---x4

# case 2
# x3---x4    x1---x2

if x2 < x3 or x4 < x1:
    print("nonintersecting")
else:
    print("intersecting")