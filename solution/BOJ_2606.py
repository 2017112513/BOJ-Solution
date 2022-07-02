def bfs(k):
    global cnt
    visited[k] = 1
    for i in graph[k]:
        if not visited[i]:
            cnt+=1
            bfs(i)

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

cnt=0

bfs(1)

print(cnt)



    
    