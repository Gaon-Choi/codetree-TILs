N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

# 목표 개수 설정
average = sum(arr) // N

result = 0

for elem in arr:
    # 목표 개수보다 적은 개수의 블록이 있는 칸만 검사
    if elem < average:
        # 부족한 만큼의 개수를 합산
        result += (average - elem)

print(result)