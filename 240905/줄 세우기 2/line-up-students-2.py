class Student:
    def __init__(self, h, w, no):
        self.h = h
        self.w = w
        self.no = no

    def __str__(self):
        return "{h} {w} {no}".format(h=self.h, w=self.w, no=self.no)

N = int(input())

arr = []

cnt = 1

for _ in range(N):
    arr.append(Student(*list(map(int, input().split())), cnt))
    cnt += 1

arr.sort(key=lambda x: (x.h, -x.w))

for elem in arr:
    print(elem)