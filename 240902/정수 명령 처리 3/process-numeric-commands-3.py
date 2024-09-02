from collections import deque

# appendleft : 맨 앞에 원소 추가
# append : 맨 끝에 원소 추가
# popleft : 맨 앞의 원소 제거
# pop : 맨 끝의 원소 제거

dq = deque()

N = int(input())

for _ in range(N):
    query = input().split()

    if query[0] == "push_front":
        dq.appendleft(int(query[1]))
    elif query[0] == "push_back":
        dq.append(int(query[1]))
    elif query[0] == "pop_front":
        print(dq.popleft())
    elif query[0] == "pop_back":
        print(dq.pop())
    elif query[0] == "size":
        print(len(dq))
    elif query[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif query[0] == "front":
        print(dq[0])
    elif query[0] == "back":
        print(dq[-1])