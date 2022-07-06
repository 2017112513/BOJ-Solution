import sys
from itertools import combinations, permutations
input = sys.stdin.readline

N = int(input())
arr = sorted([list(input().split()) for _ in range(N)],key=lambda x: -int(x[1]))     

c = list(permutations(range(1,10),3))

for num,strike,ball in arr:
    new_c = []
    while c:
        
        s,b = 0,0
        c_lis = c.pop()
        
        for i in range(3):
            if int(num[i]) == c_lis[i]:
                s+=1
            elif int(num[i]) in c_lis:
                b+=1
        if s==int(strike) and b==int(ball):
            new_c.append(c_lis)

    c= new_c


print(len(c))