def bfs(X):
    visited[X] = 1
    d = deque()
    d.append(X)

    while d:
        x = d.popleft()
        for i in dic[x]:
            if not visited[i]:
                visited[i] = 1
                d.append(i)

from collections import deque,defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0]*(n+1)
answer = 0

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        answer+=1
print(answer)

    
    
    