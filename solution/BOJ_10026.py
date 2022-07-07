def bfs(i,j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    d = deque()
    d.append([i,j,graph[i][j]])
  
    while d:
        x,y,target = d.popleft()
        for k in range(4):
            a = x+dx[k]
            b = y+dy[k]
            if 0<=a<N and 0<=b<N and graph[a][b] == target:
                if not visited[a][b]:
                    visited[a][b] = 1
                    d.append([a,b,target])
        
    dic[target]+=1

def bfs_colorx(i,j):

    flag = False
    if graph[i][j] == 'R' or graph[i][j] == 'G' :
        flag = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    d = deque()
    d.append([i,j,graph[i][j]])
    
    while d:
        # print(d)
        x,y,target = d.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N:
                if flag:
                    if graph[a][b] == 'R' or graph[a][b] == 'G':
                        if not visited_colorx[a][b] :
                            visited_colorx[a][b] = 1
                            d.append([a,b,target])
                else:
                    if graph[a][b] == 'B':
                        if not visited_colorx[a][b]:
                            visited_colorx[a][b] = 1
                            d.append([a,b,target])
                
    dic_colorx[target]+=1


from collections import deque ,defaultdict
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(input().strip()) for _ in range(N)]

dic = defaultdict(int)
dic_colorx = defaultdict(int)

visited = [[0]*N for _ in range(N)]
visited_colorx = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
        
            bfs(i,j)
            
        if not visited_colorx[i][j]:
        
            bfs_colorx(i,j)


print(sum(dic.values()),sum(dic_colorx.values()))