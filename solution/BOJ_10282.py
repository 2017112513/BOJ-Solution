import sys
from collections import defaultdict
from heapq import heappush,heappop

def dijkstra(C):

    h=[(0,C)]
    
    visited = [INF] * (N+1)

    visited[C] = 0

    while h:
        time,node = heappop(h)
        
        if visited[node]<time:
            continue

        for next_time , next_node in dic[node]:
            
            temp = next_time + time

            
            if temp < visited[next_node]: 
                visited[next_node] = temp
                heappush(h,(temp,next_node))

    return visited
            

if __name__ == '__main__':
    
    input = sys.stdin.readline
    T = int(input())

    INF = 1e9

    for _ in range(T):
        N,D,C = map(int,input().split())

        dic = defaultdict(list)
        for i in range(D):
            a,b,s = map(int,input().split())
            dic[b].append((s,a))
        answer = dijkstra(C)

        answer = [i for i in answer if i != INF]
        print(len(answer),max(answer))