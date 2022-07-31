def bfs():
    global answer ,flag 
    while d:
        t,x,y,gram = d.popleft()

        if [x,y] == [N-1,M-1]:
            flag = True
            answer = min(answer,t)
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
        
            if 0<=a<N and 0<=b<M and not visited[gram][a][b]:
                
                if arr[a][b] == 1:
                    visited[gram][a][b] = 1
                else:
                    if arr[a][b] == 2:
                        visited[gram][x][y]  = 1
                        if abs(a-N+1)+abs(b-M+1) + t + 1 <=T:
                            
                            answer = min(answer, abs(a-N+1)+abs(b-M+1) + t + 1)
                        
                            flag = True
                    else:
                        visited[gram][a][b] = 1
                        if t == T:
                            continue
                        d.append([t+1,a,b,gram])
                    


from collections import deque
import sys
input = sys.stdin.readline
N,M,T = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
answer = float('inf')

dx = [1,-1,0,0]
dy = [0,0,1,-1]

d = deque()
d.append([0,0,0,0]) # T x y gram

flag = False

visited = [[[0]*M for i in range(N)] for _ in range(2)]
visited[0][0][0] = 1

bfs()

if flag:
    print(answer)
else:
    print('Fail')


# 4 4 10
# 0 0 0 0
# 0 0 1 0
# 0 1 2 1
# 0 0 0 0
# 8