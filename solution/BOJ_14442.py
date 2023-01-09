def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def bfs():

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visited = [[[0]*M for _ in range(N)] for _ in range(10)]

    d = deque()
    d.append((1,0,0,0))

    visited[0][0][0] = 1

    while d:
        cnt,x,y,block = d.popleft()
        

        if x == N-1 and y == M-1:
            return True,cnt

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not visited[block][a][b]:
                if arr[a][b] == '0':
                    visited[block][a][b] = 1
                    d.append((cnt+1,a,b,block))

                else:
                    if block<K and not visited[block+1][a][b]:
                        visited[block+1][a][b] = 1
                        d.append((cnt+1,a,b,block+1))

    return False,-1
                
                



if __name__ == '__main__':
    import sys
    from collections import deque,defaultdict

    input = sys.stdin.readline

    N,M,K = map(int,input().split())

    arr = [list(input().strip()) for _ in range(N)]

    flag,answer = bfs()


    print(answer)