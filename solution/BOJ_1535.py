import sys
from itertools import product
input = sys.stdin.readline

N = int(input())

L = list(map(int,input().split()))
J = list(map(int,input().split()))



lis  = [[0,1] for _ in range(N)]

p = list(product(*lis)) 

answer = 0
for temp_list in p: # O(2^N) * O(N)
    hp = 100
    happy = 0
    temp = 0
    for idx,i in enumerate(temp_list):
        if i == 1:
            hp -= L[idx]
            happy += J[idx]
    if hp>0:
        answer = max(answer,happy)

print(answer)