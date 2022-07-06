from heapq import heappush,heappop
import sys
input = sys.stdin.readline
N = int(input().strip())

h = []

answer = []
for _ in range(N):
    
    n = int(input().strip())
    if n == 0:
        if h:
            x,y=heappop(h)
            print(x*y)
            # answer.append(x*y)
        else:
            print(0)
            # answer.append(0)
    else:
        if n<0:
            t = -1
        else:
            t = 1
        heappush(h,[abs(n),t])

