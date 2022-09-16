def bfs_zero(i,j):

    inner= []
    inner.append([i,j])
    d = deque()
    flag = True # 끝날때까지 True이면, 치즈 내부의 공간임 
    d.append([i,j])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while d:
        x,y = d.popleft()

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<M:
                if visited_zero[a][b] == 0 and arr[a][b] == 0:
                    visited_zero[a][b] = 1
                    inner.append([a,b])
                    d.append([a,b])

            else:
                flag = False
                if visited_zero[a][b] == 0 and arr[a][b] == 0:
                    visited_zero[a][b] = 1
                    d.append([a,b])

    
    if flag:
        return inner
    else:
        return []

    
    

def bfs_one():

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    cs_to_air = []

    while one:
        x,y = one.popleft()
        # print(x,y,'=======================')
        cnt = 0
        for i in range(4):
            
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<M and arr[a][b]==0:
                if total_inner[a][b] == 0:
                    cnt+=1
                    # print(a,b,'에 공기 있음',arr[a][b])
                    if cnt==2:
                        cs_to_air.append([x,y])
                        break
        
    # print(cs_to_air)
    return cs_to_air 

    




import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]


answer = 0

while True:
    # for z in arr:
    #     print(z)
    # print()
    is_cheese = True
    total_inner = [[0]*M for _ in range(N)]
    zero = deque()
    visited_zero = [[0]*M for _ in range(N)]
    one = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not visited_zero[i][j]:
                visited_zero[i][j] = 1
                inner_list = bfs_zero(i,j)
                for ix,iy in inner_list:
                    total_inner[ix][iy] = 1 # 1이면 내부 공기라는 의미 
            elif arr[i][j] == 1:
                is_cheese = False
                one.append([i,j])

    
    if is_cheese:
        break

    cta = bfs_one() # cs_to_air

    for i,j in cta:
        arr[i][j] = 0


    answer+=1 

    # if input() == '':
    #     pass
print(answer)


    

    
                