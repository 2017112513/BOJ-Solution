def bfs(x,y):

    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]

    visited = [[0]*N for _ in range(N)]
    
    h = []
    heappush(h,[0,x,y]) # cnt , x ,y  : 목적지까지의 최소 이동 횟수를 구하기 때문에 heap로 정렬하면서 사용
    visited[x][y] = 1
    
    while h:
        
        cnt,x,y = heappop(h)
        
        if x == end_x and y == end_y:
            return cnt
        for i in range(8):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<N and not visited[a][b]:
                visited[a][b] = 1
                heappush(h,[cnt+1,a,b])
        

from collections import deque
from heapq import heappush,heappop
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())

    answer = bfs(start_x,start_y)
    print(answer)