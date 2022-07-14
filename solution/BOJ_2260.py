def bfs(start_x,start_y):
    h = []
    visited = [[[0]*M for _ in range(N)] for i in range(2)]
    heappush(h,[1,start_x,start_y,0,visited])
    while h:
        cnt,x,y,flag,visited = heappop(h)
        if x==N-1 and y==M-1:
            print(cnt)
            exit()
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<M and not visited[flag][a][b]:
                if arr[a][b] == '1':
                    if flag==0:
                        visited[1][a][b] = 1
                      
                        heappush(h,[cnt+1,a,b,1,visited])
                    else:
                        continue
                else:
                    if flag==0:
                        visited[0][a][b] = 1
                        visited[1][a][b] = 1
                        heappush(h,[cnt+1,a,b,flag,visited])
                    else:
                        visited[1][a][b] = 1
                        heappush(h,[cnt+1,a,b,flag,visited])

from heapq import heappop,heappush
import sys
input = sys.stdin.readline 

N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

start_x,start_y = 0,0

bfs(start_x,start_y)



print(-1)