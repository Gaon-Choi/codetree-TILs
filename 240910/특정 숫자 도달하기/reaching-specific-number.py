num_list = list(map(int, input().split()))

tmp = []

for elem in num_list:
    if elem >= 250:
        break
    else:
        tmp.append(elem)

print(sum(tmp), format(round(sum(tmp) / len(tmp), 1), ".1f"))