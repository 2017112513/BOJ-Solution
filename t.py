import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(10**6+1)

dp[1] = 0
dp[2] = 1
dp[3] = 1

if n<=3:
    print(dp[n])
else:
    for i in range(4,n+1):
        
        if i%3 == 0:
            if i%2 == 0:
                dp[i] = min(dp[i-1],dp[i//2],dp[i//3]) + 1
            else:
                dp[i] = min(dp[i-1],dp[i//3]) + 1
        elif i%2 == 0: 
            dp[i] = min(dp[i-1],dp[i//2]) + 1

        else:
            dp[i] = dp[i-1]+1


    print(dp[n])


