import sys
from collections import deque



def is_inner(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def bfs():

    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    
    visited = [[0] * N for _ in range(N)]
    d = deque()
    d.append((0,start_x,start_y)) # count, x, y 

    while d:
        cnt,x,y = d.popleft()
        if x == end_x and y == end_y:
            return cnt 
        for i in range(8):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not visited[a][b]:
                visited[a][b] = 1
                d.append((cnt+1,a,b))        

     

if __name__ == '__main__':
    
    input = sys.stdin.readline
    for _ in range(int(input())):
        N = int(input())
        start_x,start_y = map(int,input().split())
        end_x,end_y = map(int,input().split())
        
        answer = bfs()
        print(answer)


