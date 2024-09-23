def is_intersection(line1, line2):
    if line1[1] < line2[0] or line2[1] < line1[0]:
        return False
    return True


n = int(input())

line_list = []

total_number = 0

for _ in range(n):
    line_list.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            except_three = [elem for idx, elem in enumerate(line_list) if ((idx != i) and (idx != j) and (idx != k))]

            is_ = True

            if len(except_three) == 1:
                total_number += 1
            else:
                for p in range(len(except_three) - 1):
                    if is_intersection(except_three[p], except_three[p + 1]):
                        is_ = False
                        break
                total_number += 1 if is_ else 0

print(total_number)