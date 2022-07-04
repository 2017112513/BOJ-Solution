def bfs(n,array):
    
    flag = True
    d = deque()
    d.append([0,0])
    start = array[0][0]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    while d:
        x,y = d.popleft()
        
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<n and not visited[a][b]:
                if array[a][b]==start:
                    visited[a][b] = 1
                    d.append([a,b])
                else:
                    flag= False
                    break
        if not flag:
            for p in range(0,n,n//2):
                
                for q in range(0,n,n//2):
                    new_array = []
                    for k in range(0,n//2,1):
                        new_array.append(array[p+k][q:q+n//2])
                    bfs(n//2,new_array)
            break
        
    if flag:
        answer[array[0][0]]+=1



from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
answer = [0]*2
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

bfs(n,arr)

print(answer[0])
print(answer[1])






        