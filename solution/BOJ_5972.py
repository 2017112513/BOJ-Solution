import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush,heappop

def dijkstra():
    h = [] 
    dic = defaultdict(list)

    for _ in range(M):
        a,b,c = map(int,input().split())
        dic[a].append((c,b))
        dic[b].append((c,a))

    visited = [1e9] * (N+1)
    visited[1] = 0
    heappush(h,(0,1))
    print(dic)
    while h:
        
        cow,x = heappop(h)

        if x == N:
            return cow
        
        for next_cow , next_x in dic[x]:
            temp = next_cow + cow
            
            if temp<visited[next_x]:
                visited[next_x] = temp
    
                heappush(h,(temp,next_x))

    print(visited)
    
if __name__ == '__main__':
    
    N,M = map(int,input().split())
    answer = dijkstra()
    print(answer)
    