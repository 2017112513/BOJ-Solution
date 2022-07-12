def get_water_cnt(x,y):
    
    cnt = 0
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        if 0<=a<N and 0<=b<M:
            if not arr[a][b]:
                cnt+=1
    return cnt



def next_day():

    d = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = get_water_cnt(i,j)
                d.append([i,j,cnt])
    
    for i,j,cnt in d:
        
        if arr[i][j]>=cnt:
            arr[i][j] = arr[i][j] - cnt
        else:
            arr[i][j] = 0

def search_ice(i,j):
    global visited
    ice_d = deque()
    ice_d.append([i,j])
    visited[i][j] = 1
    while ice_d:
        x,y = ice_d.popleft()
        
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<M and not visited[a][b]:
                visited[a][b] = 1
                if arr[a][b]:
                    ice_d.append([a,b])



import sys
from collections import deque
input=sys.stdin.readline 

N,M = map(int,input().rstrip().split())

arr = [list(map(int,input().split())) for _ in range(N)]

answer = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[0]*M for _ in range(N)]

part = False
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            if part:
                print(answer)
                exit()
            else:
                search_ice(i,j)
                part = True



while 1:

    flag = True
    visited = [[0]*M for _ in range(N)]
    next_day()
    part = False
    # for z in arr:
    #   print(z)

    answer+=1
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                flag = False
                if part:
                    print(answer)
                    exit()
                else:
                    search_ice(i,j)
                    part = True
    if flag:
        print(0)
        break

    
    
 
