def bfs():
    answer = 0
    day = 0
    
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    
    while h:
        day,z,x,y = heappop(h)
        for i in range(6):
            a,b,c, = x+dx[i] , y+dy[i] , z+dz[i]
            if 0<=a<N and 0<=b<M and 0<=c<K and not visited[c][a][b]:
                visited[c][a][b] = 1
                if arr[c][a][b] == 0:
                    arr[c][a][b] = 1
                    heappush(h,[day+1,c,a,b])

    answer = day
    return answer
        

from collections import deque
from heapq import heappop,heappush
import sys
input = sys.stdin.readline

M,N,K = map(int,input().split())

arr = [[list(map(int,input().split())) for _ in range(N)] for i in range(K)]
visited = [[[0]*M for _ in range(N)] for i in range(K)]

h = []

for k in range(K):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                h.append([0,k,i,j])
answer_day = bfs()

for k in range(K):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                print(-1)
                exit()

print(answer_day)
