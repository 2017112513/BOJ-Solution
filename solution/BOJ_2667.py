def bfs(i,j):
    
    cnt = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    d = deque()
    d.append([i,j])
    visited[i][j] = 1
    while d:
        x,y = d.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<n and not visited[a][b]:
                if arr[a][b] == '0':
                    visited[a][b] = 1
                    continue
                visited[a][b] = 1
                d.append([a,b])
                cnt+=1
    return cnt 

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
one = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            one.append([i,j])

answer = 0
cnt_list = []
for i,j in one:
    if visited[i][j] == 0:
        cnt_list.append(bfs(i,j))
        answer += 1
    else:
        continue


print(answer)
for i in cnt_list:
    print(i)