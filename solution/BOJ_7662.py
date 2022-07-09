import sys
from heapq import heappush,heappop

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())

    max_h = []
    min_h = []
    visited = [0]*(1_000_000 +1)
    for i in range(n):
        comm , num = input().rstrip().split()
        num = int(num)
        if comm == 'I':
  
            heappush(max_h,[-num,i])
            heappush(min_h,[num,i])
            visited[i] = 1
        elif comm == 'D':
            
            if num == 1:
                while max_h:
                    if visited[max_h[0][1]] == 0:
                        heappop(max_h)
                    else:
                        break
                if max_h:
                    x = heappop(max_h)
                    visited[x[1]] = 0 

            else:
                while min_h:
                    if visited[min_h[0][1]] == 0:
                        heappop(min_h)
                    else:
                        break
                if min_h:
                    x = heappop(min_h)
                    visited[x[1]] = 0

    while min_h:
                if visited[min_h[0][1]] == 0:
                    heappop(min_h)
                else:
                    break

    while max_h:
                if visited[max_h[0][1]] == 0:
                    heappop(max_h)
                else:
                    break

   

    if len(max_h) == 0:
        print('EMPTY')
    else:
        print(-heappop(max_h)[0],min(min_h)[0])

        