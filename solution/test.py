def bfs(x,y):
    d.append((x,y))
    l[x][y]=0
    while d:  
        a,b = d.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if (0<=nx<n and 0<=ny<n)and l[nx][ny]!=0:
                l[nx][ny]=0    
                d.append((nx,ny))


from collections import deque
import copy
n =int(input())
lis =[list(map(int,input().split())) for _ in range(n)]
max_rain = 0
for i in lis:
  if max_rain<=max(i):
    max_rain=max(i)


dx=[1,-1,0,0]
dy=[0,0,1,-1]
d= deque()
land=[]
for r in range(max_rain+1):
    l = copy.deepcopy(lis)
    for i in range(n):
        for j in range(n):
            if l[i][j]<=r:
                l[i][j]=0

    cnt=0
    for i in range(n):
        for j in range(n):
            if l[i][j]!=0:
        
                cnt+=1
                bfs(i,j)
        
    land.append(cnt)
print(max(land))