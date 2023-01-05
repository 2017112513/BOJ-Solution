def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
    
def bfs(sx,sy):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    d.append((0,sx,sy,0)) # count , x , y , crash
    
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]

    visited[0][sx][sy] = 1
    
    while d:
        cnt,x,y,crash = d.popleft()
        if x == Ex and y == Ey:
            return cnt

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and visited[crash][a][b] == 0:
                if arr[a][b] == 0:
                    visited[crash][a][b] = 1
                    d.append((cnt+1,a,b,crash))
                elif arr[a][b] == 1 and crash == 0:
                    visited[1][a][b] = 1
                    d.append((cnt+1,a,b,1))

    return -1 
if __name__ == '__main__':
    import sys
    from collections import deque

    input = sys.stdin.readline

    N,M = map(int,input().split())

    Hx,Hy = map(int,input().split())
    Hx,Hy = Hx-1,Hy-1

    Ex,Ey = map(int,input().split())
    Ex,Ey = Ex-1,Ey-1

    arr = [list(map(int,input().split())) for _ in range(N)]

    answer = bfs(Hx,Hy)
    print(answer)