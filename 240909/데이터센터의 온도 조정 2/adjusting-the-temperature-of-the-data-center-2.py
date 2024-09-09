def get_work_quantity(t: int, ta: int, tb: int, c, g, h):
    if t < ta:
        return c
    elif ta <= t and t <= tb:
        return g
    else:
        return h

N, C, G, H = map(int, input().split())

results = []

ta_list = []
tb_list = []
machines = []

for _ in range(N):
    Ta, Tb = map(int, input().split())

    ta_list.append(Ta)
    tb_list.append(Tb)

    machines.append([Ta, Tb])

for t in range(min(ta_list), max(tb_list) + 1):
    tmp = 0

    for machine in machines:
        tmp += get_work_quantity(t, machine[0], machine[1], C, G, H)
    
    results.append(tmp)

print(max(results))