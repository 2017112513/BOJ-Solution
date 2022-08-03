def command(n,i,x=None):
    
    print(n,i,x)
    if n == 1:
        if not arr[i][x]:
            arr[i][x] = 1
    elif n == 2:
        if arr[i][x]:
            arr[i][x] = 0
    elif n == 3:
        
        for j in range(20,0,-1):
            if arr[i][j]:
                if j == 20:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 0
                    arr[i][j+1] = 1
    else:
        for j in range(1,20+1):
            if arr[i][j]:
                if j == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 0
                    arr[i][j-1] = 1

import sys
input = sys.stdin.readline
N,M = map(int,input().split())

visited = []
arr  = [[0]*(20+1) for _ in range(N+1)]

for _ in range(M):
    comm = list(map(int,input().split()))
    if len(comm) == 3:
        n,i,x = comm[0],comm[1],comm[2]
    else:
        n,i,x = comm[0],comm[1],None
    
    command(n,i,x)

answer = 0

for a in arr:
    if a not in visited:
        visited.append(a)
        answer += 1

