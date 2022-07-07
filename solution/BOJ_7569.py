def bfs():
    answer= 0

    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]

    while tomato:
        z,x,y,day = tomato.popleft()

        answer=max(answer,day)
        for i in range(6):
            a = x+dx[i]
            b = y+dy[i]
            c = z+dz[i]
            if (0<=c<H and 0<=a<N and 0<=b<M) and not visited[c][a][b] and graph[c][a][b] == 0:
                visited[c][a][b] = 1
                graph[c][a][b] = 1
                tomato.append([c,a,b,day+1])
    
    return answer


import sys
from collections import deque
input= sys.stdin.readline

M,N,H = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

tomato = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                tomato.append([k,i,j,0]) # [z,x,y,day] 

answer = bfs()

flag = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0:
                flag = False
                break
        if not flag:
            break
    if not flag:
        break
print(answer if flag else -1 )
