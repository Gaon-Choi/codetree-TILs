def find_idx(find_arr, value):
    for i in range(len(find_arr)):
        if find_arr[i].num == value:
            return i

class NumWithOrder:
    def __init__(self, num, order):
        self.num = num
        self.order = order
        self.after_order = 0

N = int(input())

tmp_arr = list(map(int, input().split()))

arr = []
idx = 1

for i in range(len(tmp_arr)):
    arr.append(NumWithOrder(tmp_arr[i], idx))
    idx += 1

arr.sort(key=lambda number: (number.num, number.order))

for idx, elem in enumerate(arr):
    elem.after_order = idx + 1

arr.sort(key=lambda number: (number.order))

for elem in arr:
    print(elem.after_order, end=" ")