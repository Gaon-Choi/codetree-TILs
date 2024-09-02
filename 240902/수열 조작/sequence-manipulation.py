from collections import deque

dq = deque()

N = int(input())

for i in range(1, N + 1):
    dq.append(i)

while (len(dq) > 1):
    # 맨 앞의 정수 제거
    dq.popleft()

    # 남은 수열의 맨 앞의 정수를 맨 뒤로 이동
    front = dq.popleft()
    dq.append(front)

print(dq[0])