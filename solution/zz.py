# def get_max_value_case(K):
#     dp = [0] * (K + 1)

#     for weight, value in ary:
#         for i in range(K, -1, -1):
#             if i - weight < 0:
#                 break
#             dp[i] = max(dp[i - weight] + value, dp[i])
#     return dp[K]

# N, K = map(int, input().split())
# ary = [list(map(int, input().split())) for _ in range(N)]
# ary.sort()



# print(get_max_value_case(K))



n = 5
cost = [10,20,14,40,50]
x = 70


def solution(cost,x):

    LIMIT = 10**9 + 7

    dp = [0]*(x+1)

    ary = [[i,2**idx] for idx,i in enumerate(cost)]
    ary.sort()

    for weight, value in ary:

        for i in range(x, -1, -1):
            if i - weight < 0:
                break
            temp = dp[i - weight] + value 
            if temp>= LIMIT:
                temp = temp%LIMIT
            dp[i] = max(temp, dp[i])
    print(dp)
    return dp[x]

print(solution(cost,x))