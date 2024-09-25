N = int(input())

def is_exists_carry(num1, num2, num3):
    n1 = str(num1); n2 = str(num2); n3 = str(num3)

    max_size = max(len(n1), len(n2), len(n3))

    n1 = '0' * (max_size - len(n1)) + n1
    n2 = '0' * (max_size - len(n2)) + n2
    n3 = '0' * (max_size - len(n3)) + n3

    for i in range(max_size):
        if int(n1[i]) + int(n2[i]) + int(n3[i]) > 10:
            return True
    
    return False

numbers = []

for _ in range(N):
    numbers.append(int(input()))

temp = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if not is_exists_carry(numbers[i], numbers[j], numbers[k]):
                temp.append(numbers[i] + numbers[j] + numbers[k])

if temp:
    print(max(temp))
else:
    print(-1)