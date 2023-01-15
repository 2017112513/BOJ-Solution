def fibo(dp,x):
    if x <= 1:
        return x
    
    for i in range(2,x+1):
        if dp[i]<0:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[x]

    

import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (10000+1)
dp[0] , dp[1] = 0 , 1

answer = fibo(dp,N)

print(answer)