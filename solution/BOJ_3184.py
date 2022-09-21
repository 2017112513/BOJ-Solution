def bfs(i,j):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    visited[i][j] = 1
    d.append([i,j])
    cnt_s,cnt_w = 0,0

    if arr[i][j] == 'v':
        cnt_w += 1
    elif arr[i][j] == 'o':
        cnt_s +=1 

    while d:
        x,y = d.popleft()
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<M and not visited[a][b] and arr[a][b] != '#':
                visited[a][b] = 1
                if arr[a][b] == 'o':
                    cnt_s += 1
                elif arr[a][b] == 'v':
                    cnt_w += 1

                d.append([a,b])

    if cnt_s>cnt_w:
        return cnt_s,0
    else:
        return 0,cnt_w



import sys
input = sys.stdin.readline 
from collections import deque
N,M = map(int,input().split())

arr = [list(input().strip()) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

sheep,wolf = 0,0

for i in range(N):
    for j in range(M):
        if arr[i][j] != '#' and not visited[i][j]:
            # print(i,j)
            sheep_cnt,wolf_cnt = bfs(i,j)
            # print(sheep_cnt,wolf_cnt)
            sheep+=sheep_cnt
            wolf+=wolf_cnt

print(sheep,wolf)