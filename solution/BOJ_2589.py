def bfs(sx,sy):


    time = 0

    max_cnt = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    d.append([0,sx,sy])

    visited = [[0]*M for _ in range(N)]

    visited[sx][sy] = 1

    while d:
        cnt,x,y = d.popleft()

        max_cnt = max(max_cnt,cnt)

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<M and not visited[a][b] and arr[a][b] == 'L':
                visited[a][b] = 1
                d.append([cnt+1,a,b])

    return max_cnt

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]



answer_list = []
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            
            c = bfs(i,j)

            answer = max(answer,c)
          
print(answer)
