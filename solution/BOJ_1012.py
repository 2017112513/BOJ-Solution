from collections import deque
import sys
input = sys.stdin.readline

def bfs(one_x,one_y):
    d = deque()
    d.append([one_x,one_y])
    while d:
        x,y = d.popleft()
        for id in range(4):
            a = x+dx[id]
            b = y+dy[id]
            if 0<=a<m and 0<=b<n and not visited[a][b] and arr[a][b] == 1:
                visited[a][b] = 1
                d.append([a,b])

dx = [1,-1,0,0]
dy = [0,0,1,-1]        
    
for _ in range(int(input())):
    
    n,m,k = map(int,input().split())
    arr = [[0]*n for i in range(m)]
    visited = [[0]*n for i in range(m)]
    one_list = []

    for j in range(k):
        q,p = map(int,input().split())
   
        arr[p][q] = 1
        one_list.append([p,q])
    
    answer = 0
    while one_list:
        one_x,one_y = one_list.pop()
        
        if not visited[one_x][one_y]: # if visited[one_x][one_y] ==0: , 아직 방문하지 않은 점이라는 뜻 
            visited[one_x][one_y] = 1
            answer += 1 
            bfs(one_x,one_y)
    
    print(answer)

    
    
    
    
