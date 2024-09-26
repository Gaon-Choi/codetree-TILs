dp = [0] * 1001

dp[1] = 2
dp[2] = 7

for i in range(3, 1001):
    dp[i] = (dp[i - 1] + 2) + (dp[i - 2] + 7)

n = int(input())

print(dp[n] % 1000000007)