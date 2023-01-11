import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def is_inner(N,x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def search(N,guest,sx,sy,arr):

    search_list = []

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]    

    visited = [[0]*N for _ in range(N)]
    
    visited[sx][sy] = 1

    d = deque() 
    d.append((0,sx,sy)) # 거리 , Row , Col
    
    while d:
        move,x,y = d.popleft()

        if guest[x][y]:
            search_list.append([move,x,y])

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(N,a,b) and visited[a][b] == 0 and arr[a][b] != 1:
                
                visited[a][b] = 1
                d.append((move+1,a,b))
    if search_list:
        Z,X,Y = sorted(search_list,key=lambda x: (x[0],x[1],x[2]))[0]
        return X,Y,Z

    return -1,-1,-1

def bfs(N,guest,X,Y,Z,E,arr):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1] 

    if E<=Z:
        return False,-1,-1

    d = deque()
    d.append((E-Z,X,Y))
    visited = [[0]*N for _ in range(N)]
    visited[X][Y] = 1

    end_x,end_y = guest[X][Y]
  
    while d:
        fuel,x,y = d.popleft()
   
        if x == end_x and y==end_y:
            return fuel + (E-Z-fuel) * 2 ,x,y
        if fuel == 0:
            continue

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(N,a,b) and visited[a][b] == 0 and arr[a][b] != 1:
                visited[a][b] = 1
                d.append((fuel-1,a,b))
    return False,-1,-1
                
        


def main():

    N,K,E = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
 
    sx,sy = map(int,input().split())
    sx,sy = sx-1,sy-1

    guest = [[0]*N for _ in range(N)]
    
    for _ in range(K):
        a,b,c,d = map(int,input().split())
        guest[a-1][b-1] = [c-1,d-1]
    #################################################
    count = 0
    while 1:
    # 그래프를 탐색하며 가장 가까운 승객을 구한다 
        X,Y,Z = search(N,guest,sx,sy,arr)
        if X== -1:
            return -1
        # 가장 가까운 승객을 구하고 목적지까지 최단거리로 이동한다 
        E,sx,sy = bfs(N,guest,X,Y,Z,E,arr)
        if not E:
            return -1
        count += 1
        guest[X][Y] = 0

        if count == K:
            return E
    # 승객을 모두 이동시키거나, 연료가 떨어질 때까지 반복한다.

if __name__ == '__main__':

    answer = main()
    print(answer)


