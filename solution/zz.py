N = int(input())
dp = [[0 for i in range(10)]for j in range(1001)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2,N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])
print(sum(dp[N]) % 10007)