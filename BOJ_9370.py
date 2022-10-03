def if_flag(search_road , flag, new_node):
    if not flag:
        if len(search_road):
            if (search_road == str(road_1) and new_node == road_2) or (search_road == str(road_2) and new_node == road_1) : 
                search_road = ''
                flag = True
            else:
                search_road = str(new_node)
                
        else:
            search_road =str(new_node)
    return search_road , flag 
        
def dijkstra():

    weight = [float('inf')]*(n+1)
    heappush(h,[0,s,'',False]) # True면 도로를 지나왔다는 뜻  
    if_road = [False]*(n+1)
    weight[s] = 0
    while h:

        curr_wei,curr_node,search_road,flag = heappop(h)
    
        if curr_wei > weight[curr_node]:
            continue

        for new_wei,new_node in dic[curr_node]:
            wei = new_wei+curr_wei
            if weight[new_node]>=wei:
                new_search_road , new_flag = if_flag(search_road,flag,new_node)

                weight[new_node] = wei
                if_road[new_node] = new_flag

                heappush(h,[wei,new_node,new_search_road,new_flag])

    

    return weight,if_road





import sys
input = sys.stdin.readline 
from collections import defaultdict
from heapq import heappush,heappop
for i in range(int(input())):
    
    dic = defaultdict(list)
    n,m,t = map(int,input().split()) 
    s,road_1,road_2 = map(int,input().split())

    h = []

    for _ in range(m): 
        a,b,d = map(int,input().split())
        
        dic[a].append((d,b))
        dic[b].append((d,a))

    ins = [int(input()) for _ in range(t)]
    

    

    weight,if_road = dijkstra()

    if_road = [idx for idx, bl in enumerate(if_road) if bl and idx in ins]

    print(*if_road,'answer')

