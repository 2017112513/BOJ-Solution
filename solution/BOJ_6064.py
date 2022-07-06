
from re import I
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    
    N,M,X,Y = map(int,input().strip().split())
    flag = True
    for p in range(1,N*M+1):
        
        if N<M:
            if p==Y:
                continue
            if (p-Y)%M == 0:
                
                print(p,1)
                flag = False
                break        
        else:
            if p==X:
                continue
            if (p-X)%N == 0:
                print(p,2)
                flag  = False
                break
     
    if flag:
        print(-1)

