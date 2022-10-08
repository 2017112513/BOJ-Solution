def dijkstra():
    
    h = [] 
    h.append([0,s])

    weight = [int(1e9)] * (n+1)
    weight[s] = 0 

    while h:
        curr_weight , curr_node = heappop(h)

        if curr_weight>weight[curr_node]:
            continue
            
        for next_weight,next_node in dic[curr_node]:
            new_weight = curr_weight + next_weight

            if new_weight<=weight[next_node]:
                weight[next_node] = new_weight
                heappush(h,[new_weight,next_node])

    return weight


import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush,heappop

for i in range(int(input())):
    dic = defaultdict(list)
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    for _ in range(m):
        a,b,c = map(int,input().split())
        dic[a].append([c,b])
        dic[b].append([c,a]) #거리, 도착노드 

    hubo = [int(input()) for _ in range(t)]

    for i in dic[g]:
        if i[1] == h:
            i[0] -= 0.1 
        
    for i in dic[h]:
        if i[1] == g:
            i[0] -= 0.1

    weight_lst = dijkstra()
    answer = []
    for hb in hubo: 
        if type(weight_lst[hb]) is float :
            answer.append(hb)
    answer.sort()

    print('aswer',*answer)