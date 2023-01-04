import sys
from collections import defaultdict,deque


def bfs(start_x):
    
    d = deque()
    d.append((0,start_x))

    visited = [0] * (N+1)
    
    while d:
        cnt , x  = d.popleft()
        if cnt>K:
            break
        for next_x in dic[x]:
            
            if not visited[next_x] and next_x != start_x:
                visited[next_x] = cnt+1
                d.append((cnt+1,next_x))
    
    return visited

if __name__ == '__main__':

    input = sys.stdin.readline

    N,M,K,X = map(int,input().split())  # 도시 개수 , 도로 개수 , 최단 거리 , 시작 지점 
    
    dic = defaultdict(list)
    for _ in range(M):
        a,b = map(int,input().split())
        dic[a].append(b)
    
    answer_list = bfs(X)

    answer = [idx for idx,i in enumerate(answer_list) if i == K]

    if answer: 
        for i in answer:
            print(i)
    else:
        print(-1)

    