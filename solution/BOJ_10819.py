import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split())) 

bruteforce = tuple(permutations(arr,n)) # O(n!)

answer = 0

for lis in bruteforce:  # O(n!) X n  , 최대 시간 복잡도  = 8! * 8 
    temp = 0    
    for i in range(n-1):
        tmp = abs(lis[i]-lis[i+1])
        temp+=tmp
    answer = max(temp,answer)

print(answer)
