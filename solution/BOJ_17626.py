import sys
import math
input = sys.stdin.readline
dp = [0]*(50000+1)

def search_jegop_geon(n):
    sqrt_num = int(math.sqrt(n))
    return sqrt_num
dp[1] = 1

n = int(input())


    
for i in range(2,n+1):
    sqrt_num = search_jegop_geon(i)
    if sqrt_num**2==i:
        dp[i] = 1

    dp[i] = i

for j in range(sqrt_num,-1,-1):
    # print(j)
    dp[i] = min(dp[i-j*j]+1,dp[i])

print(dp[n])