from collections import defaultdict,deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

dic = defaultdict(int)

for _ in range(N+M):
    a,b = map(int,input().split())
    dic[a] = b

d = deque()
graph = [0]*(100+1)

d.append([0,1])

while d:
    cnt,x = d.popleft()
    if x == 100:
        print(cnt)
        break

    print(x)
    for i in range(1,6+1):
        if x+i>100:
            continue
        if not graph[x+i]:
            graph[x+i] = cnt+1
            if dic[x+i] and not graph[dic[x+i]]:
                graph[dic[x+i]] = cnt+1
                d.append([cnt+1,dic[x+i]])
            else:
                d.append([cnt+1,x+i])

        else:
            continue

