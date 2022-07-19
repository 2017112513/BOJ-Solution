def bfs(i,j):

    count = 1
    d = deque()
    d.append([i,j])
    visited[i][j] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while d:
        x,y = d.popleft()

        for k in range(4): 
            a,b = x+dx[k],y+dy[k]
      
            if 0<=a<N and 0<=b<N and not visited[a][b]:
                visited[a][b] = 1
                if arr[a][b] == '1':
                    d.append([a,b])
                    count += 1

    return count 

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
arr = [list(input()) for _ in range(N)]

answer = []

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == '1':
            cnt = bfs(i,j)
            answer.append(cnt)


print(len(answer))
for i in sorted(answer):
    print(i)