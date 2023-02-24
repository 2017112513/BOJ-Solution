def dfs(graph,v,visited): #7,
    
    global count

    if v==bb:

        return count
    for i in graph[v]: #2
        if not visited[i]:
            visited[i]=True 
            count+=1

            dfs(graph,i,visited)

                


from collections import deque
n=int(input())#9
aa,bb=map(int,input().split())#7,3
#부모 자식들 간의 관계의 개수 m
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

count = 0
ans = dfs(graph,aa,visited) 
print(ans)
# print(count)