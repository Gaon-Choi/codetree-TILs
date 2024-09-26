K, N = map(int, input().split())

# 1 이상 K 이하의 숫자를 하나 고르는 행위
# N번 반복함

answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer()
        return

    for num in range(1, K + 1):
        answer.append(num)
        choose(curr_num + 1)
        answer.pop()

choose(1)