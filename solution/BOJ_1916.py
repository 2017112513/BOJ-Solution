from re import L
import sys
from heapq import heappush,heappop
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

dic = defaultdict(list)

for _ in range(M):
    start,depart,cost = map(int,input().split())
    dic[start].append((cost,depart))


start,depart = map(int,input().split()) 

def dijkstra(x):

    h = []
    heappush(h,[0,x])
    weight = [float('inf')]*(N+1)
    visited = [0]*(N+1)
    weight[x] = 0
    
    while h :
        
        curr_cost,curr_node = heappop(h) 
        

        if weight[curr_node]<curr_cost:
            continue

        for next_cost,next_node in dic[curr_node]:
            sum_cost = next_cost + curr_cost

            if sum_cost<weight[next_node]:
                weight[next_node] =  sum_cost
                print(curr_cost,curr_node,next_node)
                heappush(h,[sum_cost,next_node])

    return weight
answer = dijkstra(start)
print(answer[depart])
