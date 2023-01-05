def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def gram(x,y):
    return abs(N-1-x) + abs(M-1-y)

def bfs():

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d= deque()
    d.append((0,0,0)) # T , X , Y 
    visited = [[0]* M for _ in range(N)]
    visited[0][0] = 1
    temp = int(10**9)
    
    while d:
        t,x,y = d.popleft()

        if x == N-1 and y == M-1:

            answer=min(t,temp)

            if answer <= T:
                return answer

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not visited[a][b] and arr[a][b] != 1:
                if arr[a][b] == 0:
                    visited[a][b] = 1
                    d.append((t+1,a,b))
                else:
                    visited[a][b] = 1
                    temp = t + gram(a,b) + 1 
                    if temp <= T :
                        answer= temp
  
    if temp <= T : 
        return temp 

    return False
                    
                 

if __name__ == '__main__':
    import sys
    from collections import deque


    input = sys.stdin.readline

    N,M,T = map(int,input().split())
    
    arr = [list(map(int,input().split())) for _ in range(N)]

    answer = bfs()

    print(answer if answer else "Fail")