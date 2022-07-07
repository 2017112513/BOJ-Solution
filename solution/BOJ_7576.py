def bfs():
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while tomato:

        x,y,day = tomato.popleft()
        answer = max(answer,day)

        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<M and not visited[a][b] and graph[a][b] == 0:
                visited[a][b] = 1
                graph[a][b] = 1

                tomato.append([a,b,day+1])
    return answer

import sys
from collections import deque

input = sys.stdin.readline
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
tomato = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append([i,j,0])
            visited[i][j] = 1

flag = True

answer= bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = False
            break

print(answer if flag else -1)


