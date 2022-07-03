from tracemalloc import start


def bfs(start_point):

    answer = []
    d = deque()
    d.append(start_point)
    visited = [0]*(n+1)
    visited[start_point] = 1
    answer.append(start_point)
    while d:
        x = d.popleft()
        for i in dic[x]:
            
            if not visited[i]:
                visited[i] = 1
                answer.append(i)
                d.append(i)
    return answer

def dfs(start_point):
    visited[start_point] = 1
    print(dic)
    for i in dic[start_point]:
        if not visited[i]:
            print(i)
            answer.append(i)
            dfs(i)
    return answer
  

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

n,m,start_point = map(int,input().split())

dic = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

for key in dic.keys():
    dic[key] = sorted(dic[key])

answer_bfs = bfs(start_point)


answer = []
visited = [0]*(n+1)
answer.append(start_point)
answer_dfs = dfs(start_point)


for i in answer_dfs:
    print(i,end=' ')
print()
for i in answer_bfs:
    print(i,end=' ')
print()