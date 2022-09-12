
def bfs():
    
    d = deque()
    d.append([0,S]) # cnt, S 
    visited = [0]*(F+1)
    visited[S] = 1
    df = [U,-D]
    while d:
        cnt,curr_floor = d.popleft()
        if curr_floor == G:
            return cnt 
        for i in range(2):
            next_floor = curr_floor+df[i]
            if 1<=next_floor<=F and not visited[next_floor]:
                visited[next_floor] = 1
                d.append([cnt+1,next_floor])

    return "use the stairs"
        

import sys
from collections import deque
input = sys.stdin.readline

# F: 전체 층수
# S: 현재 층수 
# G: 목적지 
# U: 위층으로 U만큼
# D: 아래층으로 D만큼 

F,S,G,U,D = map(int,input().split()) 
answer = bfs()

print(answer)



