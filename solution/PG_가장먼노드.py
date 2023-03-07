from collections import defaultdict
from heapq import heappush , heappop

def dijkstra(n,dic):
    
    INF = 10**9
    h = [(0,1)] 
    visited = [INF]*(n+1)
    visited[1] = 0

    while h:
        weight , node = heappop(h)
        
        for next_node in dic[node]:
            
            if visited[next_node] > weight + 1: 
                
                visited[next_node] = weight + 1
                heappush(h,(weight+1 , next_node))
    return visited
    

def solution(n, edge):
    
    
    
    dic = defaultdict(list)
    
    for a,b in edge: 
        dic[a].append(b)
        dic[b].append(a)
    
    temp = dijkstra(n,dic)
    temp = temp[1:]
    
    answer = temp.count(max(temp))
    
    return answer