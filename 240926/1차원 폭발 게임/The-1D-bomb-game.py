N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

while True:
    temp = []

    tmp = []

    prev = arr[0]

    for elem in arr:
        if elem == prev:
            tmp.append(elem)

        else:
            temp.append(tmp)
            tmp = [elem]
            prev = elem

    if tmp:
        temp.append(tmp)

    is_flag = False
    for pair in temp:
        if len(pair) >= M:
            is_flag = True

    answer = []

    for pair in temp:
        if len(pair) < M:
            answer.extend(pair)

    arr = answer

    if not is_flag or not arr:
        break
        
print(len(answer))
for elem in answer:
    print(elem)