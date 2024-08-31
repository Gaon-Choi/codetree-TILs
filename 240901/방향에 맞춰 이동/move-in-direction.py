curr_x = 0
curr_y = 0

dxdy = {
    "N": (0, +1),
    "S": (0, -1),
    "E": (+1, 0),
    "W": (-1, 0)
}

N = int(input())

for _ in range(N):
    D, offset = input().split()
    curr_x += dxdy[D][0] * int(offset)
    curr_y += dxdy[D][1] * int(offset)
    
print(curr_x, curr_y)