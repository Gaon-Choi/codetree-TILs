N = input()
N = N[-1::-1]

decimal_result = 0

for weight, value in enumerate(N):
    if value == "1":
        decimal_result += (2 ** weight)

decimal_result *= 17

print(str(bin(decimal_result))[2:])