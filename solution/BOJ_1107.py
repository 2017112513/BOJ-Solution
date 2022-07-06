
from itertools import product
import sys
input = sys.stdin.readline

N = input().strip()
n = input().strip()

if n!='0':
    error = list(map(int,input().split()))
else:
    error = []
num_list = [i for i in range(0,10) if i not in error]
curr = 100
answer = abs(int(N)-curr)
for l in range(1,7):
    c = list(product(num_list,repeat = l))
    # print(c)
   
    for i in c:
   
        cnt  = 0
        n = 10**(len(i)-1)
        s = 0
        for k in i:

            s += k*n
            n = n//10
       
        cnt=len(str(s))
        target = int(N)
   
        if target>s:
            answer = min(answer,target-s+cnt)
            
        else: 
            answer = min(answer,s-target+cnt)

       
print(answer)
