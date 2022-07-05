def bfs(vis,d):
    
    while d:
        x,y = d.popleft()
        for k in range(4):
            a = x+dx[k]
            b = y+dy[k]
          
            if 0<=a<n and 0<=b<m and vis[a][b] == 0:
                if arr[a][b] == 1:
                    vis[a][b] = 1
                else:
                    vis[a][b] = 1
                    d.append([a,b])
    return vis




from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0

d = deque()
blank = []
w = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            d.append([i,j])
        
        elif arr[i][j] == 0:
            blank.append([i,j])
        else:
            w.append([i,j])
c = combinations(blank,3)



for wall in c:
    
    copy_d = deepcopy(d)
    visited = [[0]*m for _ in range(n)]
    for i,j in wall:
        visited[i][j] = 1
    for i,j in w:
        visited[i][j] = 1
    for i,j in d:
        visited[i][j] = 1

  
    vis = bfs(visited,copy_d)

    M = 0 
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0:
                M+=1

    answer = max(answer,M)
print(answer)

    
    

