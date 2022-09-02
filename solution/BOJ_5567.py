import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

from collections import defaultdict,deque
dic = defaultdict(list)

for _ in range(M):
    a,b =map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)


d = deque

def bfs():
    visited = [0]*(N+1)
    d = deque()
    d.append([1,0]) # start point,cnt
    visited[1] = 1

    while d:
        x,cnt = d.popleft()
        for friend in dic[x]:
            if not visited[friend] and cnt<2:
                visited[friend] = 1
                d.append([friend,cnt+1])

    return visited

v = bfs()

print(v.count(1)-1)




        
