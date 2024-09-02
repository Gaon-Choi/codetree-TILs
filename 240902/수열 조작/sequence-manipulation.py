queue = list()

N = int(input())

for i in range(1, N + 1):
    queue.append(i)

while (len(queue) > 1):
    # 맨 앞의 정수 제거
    queue.pop(0)

    # 남은 수열의 맨 앞의 정수를 맨 뒤로 이동
    front = queue.pop(0)
    queue.append(front)

print(queue[0])