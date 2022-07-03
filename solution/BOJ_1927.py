from heapq import heappush,heappop
import sys
input = sys.stdin.readline 

n = int(input())
h = []

for _ in range(n):
    m = int(input())
    if m == 0:
        if h:
            print(heappop(h))
        else:
            print(0)
    else:
        heappush(h,m)