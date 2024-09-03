dx = {
    "N": 0,
    "E": +1,
    "S": 0,
    "W": -1
}

dy = {
    "N": +1,
    "E": 0,
    "S": -1,
    "W": 0
}

curr_x = 0
curr_y = 0

N = int(input())

for _ in range(N):
    query = input().split()
    curr_x += dx[query[0]] * int(query[1])
    curr_y += dy[query[0]] * int(query[1])
    
print(curr_x, curr_y)