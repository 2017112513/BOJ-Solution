
def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while h:
        cnt,x,y = heappop(h)
        if x==n-1 and y==m-1:
            return cnt
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m and not visited[a][b]:
                if arr[a][b] == '0':
                    continue
                visited[a][b] = 1
                heappush(h,[cnt+1,a,b])

from heapq import heappush,heappop
import sys
input = sys.stdin.readline 

n,m = map(int,input().split()) 
arr = [list(input()) for _ in range(n)]

h = []

visited = [[0] * m for _ in range(n)]
heappush(h,[1,0,0]) # cnt, x, y
answer = bfs()
print(answer)

