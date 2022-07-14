

def f(i,x,y):
    while 0<=x+dx[i]<N and 0<=y+dy[i]<N:
        a,b = x+dx[i],y+dy[i]
        if lis[a][b] == 0:
            lis[a][b] = lis[x][y]
            lis[x][y] = 0
            # print(x,y,'->',a,b,lis[a][b],)
        elif lis[a][b] == lis[x][y]:
            if visited_hap[a][b] == 0  and visited_hap[x][y] == 0:
                lis[a][b] = 2*lis[x][y]
                lis[x][y] = 0   
                visited_hap[a][b] = 1
                # print(x,y,'->',a,b,lis[a][b],)
        else:
            break
        x,y = a,b

def solution(i):
    if i == 0:
        for x in range(N):
            for y in range(N):
                f(i,x,y)
        if lis not in visited:
                visited.append(lis)
                d.append([lis,cnt+1])

    elif i == 1:
        for x in range(N-1,-1,-1):
            for y in range(N):
                f(i,x,y)
        if lis not in visited:
                visited.append(lis)
                d.append([lis,cnt+1])


    elif i == 2:
        for y in range(N-1,-1,-1):
            for x in range(N-1,-1,-1):
                f(i,x,y)
        if lis not in visited:
                visited.append(lis)
                d.append([lis,cnt+1])
        
    elif i == 3:
        for y in range(N):
            for x in range(N):
                f(i,x,y)
        if lis not in visited:
                visited.append(lis)
                d.append([lis,cnt+1])

    

import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

answer = 0

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1] 

d = deque()
d.append([arr,0]) 

visited = []

while d:
    arr,cnt = d.popleft()

    for i in range(N):
        answer = max(max(arr[i]),answer)
    if cnt ==5:
        continue

    for i in range(4):
        lis = deepcopy(arr)
        visited_hap = [[0]*N for _ in range(N)]
        solution(i)




print(answer)