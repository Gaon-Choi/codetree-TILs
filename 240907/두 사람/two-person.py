y1, g1 = input().split()
y2, g2 = input().split()

y1 = int(y1); y2 = int(y2)

if (y1 >= 19 and g1 == "M") or (y2 >= 19 and g2 == "M"):
    print(1)
else:
    print(0)