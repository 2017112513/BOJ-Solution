
import sys
input=sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
 
        if i==0 and j==0:
            continue
        if i==0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
            continue
        if j==0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
            continue
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + arr[i][j]
            continue
print(dp[n-1][m-1])