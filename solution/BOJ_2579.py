import sys
input = sys.stdin.readline
n = int(input())
stair = [int(input()) for _ in range(n)]

def solution(n):
    dp = [0]*(n)
    dp[0] = stair[0]
    if n==1:
        return dp[0]
    elif n==2:
        dp[1] = dp[0] + stair[1]
        return dp[1]
    elif n==3:
        dp[2] = stair[2] +max(stair[1],stair[0])
    else:
        dp[1] = dp[0] + stair[1]
        dp[2] = stair[2] +max(stair[1],stair[0])
        for i in range(3,n):
            dp[i] = stair[i] + max(dp[i-2],stair[i-1]+dp[i-3])
        return dp[n-1]
answer = solution(n)
print(answer)
