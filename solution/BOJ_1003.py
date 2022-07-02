import sys
input = sys.stdin.readline

dp = [0]*(40+1)

dp[0] = [1,0]
dp[1] = [0,1]

for i in range(2,40+1):
    dp[i]=[dp[i-1][0]+dp[i-2][0] , dp[i-1][1]+dp[i-2][1]]

for _ in range(int(input().strip())):
    n = int(input().strip())
    print(dp[n][0],dp[n][1])