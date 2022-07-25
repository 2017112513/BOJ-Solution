
def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for k in range(4):
        a,b = x+dx[k],y+dy[k]
        if 0<=a<N and 0<=b<M:
            bom_list[a][b] = 0

def wait():  # O(N^2)
    global time
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'O':
                bom_list[i][j] = 2 # 1초 동안 쉬는 시간이라서 폭탄의 제한시간은 2초로 줄어듬
    time+=1
    
def search_bomb(): # O(N^2)

    global time
    global d

    for i in range(N):
        for j in range(M):
            if bom_list[i][j]:
                bom_list[i][j] -= 1
                if bom_list[i][j] == 0:
                    d.append([i,j])
            else:
                bom_list[i][j] = 3

    time+=1

def boom():
    for i in range(N):
        for j in range(M):
            if bom_list[i][j] == 1:
                bom_list[i][j] = 0
                d.append([i,j])
            elif bom_list[i][j]>1:
                bom_list[i][j] -= 1
    while d:
        x,y = d.popleft()
        bom_list[x][y] = 0
        bfs(x,y)
# ------------- main -----------------------

import sys
from collections import deque
input = sys.stdin.readline

N,M,target_time = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
bom_list =[[0]*M for _ in range(N)]

if target_time == 1:
    for z in graph:
        print(''.join(z))
else:

    d = deque()
    time = 0

    wait()
    while True:

        search_bomb() # 3단계 함수
        if time == target_time:
            break

        boom() # 4단계 함수

        time+=1
        if time == target_time:
            break

    for i in range(N):
        for j in range(M):
            if bom_list[i][j]:
                print('O',end='')
            else:
                print('.',end='')
        print()