dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 3

N = int(input())

for i in range(4, N + 1):
    dp[i] = (dp[i-2] + 4) + (dp[i-1] + 2)

print(dp[N] % 10007)