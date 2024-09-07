class Point:
    # white : 0, black : 1, gray : 2

    def __init__(self):
        self.coloring = []
    
    def add_color(self, color):
        self.coloring.insert(0, color)

    def get_curr_color(self):
        if self.coloring.count(0) >= 2 and self.coloring.count(1) >= 2:
            return 2
        elif len(self.coloring) >= 1:
            return self.coloring[0]
        else:
            return None


N = int(input())

arr = [Point() for _ in range(100000)]

offset = len(arr) // 2

curr = 0

for _ in range(N):
    dist, direction = input().split()
    dist = int(dist)

    if direction == "R":
        for i in range(dist):
            arr[curr + i].add_color(1)
        curr = curr + (dist - 1)
    else:
        for i in range(dist):
            arr[curr - i].add_color(0)
        curr = curr - (dist - 1)

result = [0, 0, 0]

for elem in arr:
    idx = elem.get_curr_color()
    if idx is not None:
        result[idx] += 1

print(result[0], result[1], result[2])