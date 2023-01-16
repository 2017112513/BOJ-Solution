N = int(input())
dp = [[1] * 10 for _ in range(N+1)]

for i in range(1,N+1):
    if i == 1 :
        continue
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[N])%10007)
        

