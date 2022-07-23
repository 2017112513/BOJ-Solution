import sys
from collections import defaultdict
from heapq import heappush,heappop

input = sys.stdin.readline

N,M = map(int,input().split())
start_x = int(input())

graph = [float('INF')]*(N+1)
graph[start_x] = 0

dic = defaultdict(list)
h = []

for _ in range(M):
    
    u,v,w = map(int,input().split())

  
    dic[u].append([w,v])

heappush(h,[graph[start_x],start_x])


while h:
    distance,curr_node = heappop(h)
    if distance>graph[curr_node]:
        continue
    
    for new_weight, new_node in dic[curr_node]:
        new_distance = distance+new_weight
        if new_distance<graph[new_node]:
            graph[new_node] = new_distance
            heappush(h,[new_distance,new_node])



for i in graph[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

    


    
