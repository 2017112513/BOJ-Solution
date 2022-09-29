from re import L
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
minh= []
maxh= []

mid = 0
for idx,_ in enumerate(range(N)):

    n = int(input())

    if idx == 0:
        mid = n
        
    elif idx == 1:
        if n<mid:
            heappush(minh,n)
            heappush(maxh,(-1,-1*mid))
            mid = n
        else:
            heappush(minh,mid)
            heappush(maxh,(-1,-1*n))
    else:
        if n<mid:
            heappush(minh,n)
        else:
            heappush(maxh,(-1,-1*n))

    
    print('minh',minh)
    print('maxh',maxh)
    
