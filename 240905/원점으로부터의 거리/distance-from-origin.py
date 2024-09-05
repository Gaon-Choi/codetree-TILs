class Point:
    def __init__(self, num, x, y):
        self.num = num
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "{x} {y}".format(x=self.x, y=self.y)

points = []

N = int(input())

for i in range(N):
    points.append(Point(i+1, *input().split()))

points.sort(lambda point : (abs(point.x) + abs(point.y), point.num))

for point in points:
    print(point.num)