import sys
from collections import defaultdict
from heapq import heappush , heappop

def dijkstra(i):
    INF = 999
    visited = [INF] * N 
    answer  = [INF] * N 
    tdic = defaultdict(int)
    
    h = [(0,i,[])]

    visited[i] = 0
    answer[i] = '-'

    while h:
        
        weight , node , lis = heappop(h)
        
        for next_weight, next_node in dic[node]:

            temp = next_weight + weight
            
            if temp < visited[next_node]:

                # print(node,next_node,temp)       
                visited[next_node] = temp
                
                if lis:
                    answer[next_node] = lis[0] + 1
                    heappush(h,(temp,next_node,lis))
                else: 
                    answer[next_node] = next_node+1
                    heappush(h,(temp,next_node,[next_node]))



    return visited,answer 
    


if __name__ == '__main__':
    
    N,K = map(int,input().split())
    
    dic = defaultdict(list)
    
    for _ in range(K):
        a,b,c = map(int,input().split())
        
        dic[a-1].append((c,b-1))
        dic[b-1].append((c,a-1))
    # print('================================================')
    for i in range(N):
        visited,answer = dijkstra(i)
        print(*answer)