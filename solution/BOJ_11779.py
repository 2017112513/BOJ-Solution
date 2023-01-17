import sys
from collections import defaultdict
from heapq import heappush,heappop


def dijkstra(startpoint,endpoint):

    h = [] 
    heappush(h,(0,startpoint))
    
    visited = [1e9] * (N+1)
    visited[startpoint] = 0

    cnt_list = [0] * (N+1)


    while h:

        weight, node = heappop(h)
        
        if visited[node] < weight:
            continue

        if node == endpoint:
            break 

        for next_weight , next_node in dic[node]:

            temp = next_weight + weight 

            if temp < visited[next_node]:
                visited[next_node] = temp
                cnt_list[next_node] = node # cnt_list[도착점] = 시작점
                heappush(h,(temp,next_node))

    return weight,cnt_list

def rolling(cnt_list,x):
    
    answer = [] 
    
    while 1:
        answer.append(x)

        x = cnt_list[x]

        if x == 0:
            break

    return answer
        



if __name__ == '__main__':
    input = sys.stdin.readline
    
    N = int(input())
    M = int(input())

    dic = defaultdict(list)
    
    for _ in range(M):
        a,b,c = map(int,input().split())
        dic[a].append((c,b))
    
    startpoint,endpoint = map(int,input().split())

    answer_weight, cnt_list = dijkstra(startpoint,endpoint)
    answer_node = rolling(cnt_list,endpoint)
    
    print(answer_weight)
    print(len(answer_node))
    print(*answer_node[::-1])
    

    
    

