import sys
from heapq import heappush,heappop
from collections import deque , defaultdict


def dijkstra(start):

    h = [(0,start)]
    
    visited = [1e9] * (N+1)
    visited[start] = 0

    while h:
        weight,node = heappop(h)

        for next_weight, next_node in dic[node]:
            temp = weight+next_weight
            if temp <= M and temp<visited[next_node]:
                visited[next_node] = temp
                heappush(h,(temp,next_node))

    answer = sum([items[i] for i in range(1,N+1) if visited[i]<=M])

    return answer 
                    

        
    
    
                





if __name__ == '__main__':
    input = sys.stdin.readline
    N,M,R = map(int,input().split())
    items = deque(map(int,input().split()))
    items.appendleft(0)

    dic = defaultdict(list)
    for _ in range(R):
        a,b,c = map(int,input().split())
        dic[a].append((c,b))
        dic[b].append((c,a))

    final_answer = 0

    for i in range(1,N+1):

        answer = dijkstra(i)
        final_answer = max(final_answer,answer)
    
    print(final_answer)

    