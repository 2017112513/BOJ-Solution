
def command(n,i,x):
    if n == 1:
        if not arr[i][x]:
            arr[i][x] = 1
    elif n == 2:
        if arr[i][x]:
            arr[i][x] = 0
    elif n == 3:
        
        for j in range(19,-1,-1):
            if arr[i][j]:
                if j == 19:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 0
                    arr[i][j+1] = 1
    else:
        for j in range(0,20):
            if arr[i][j]:
                if j == 0:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 0
                    arr[i][j-1] = 1

import sys
input = sys.stdin.readline
N,M = map(int,input().split())

visited = []
arr  = [[0]*(20) for _ in range(N)]

for _ in range(M):
    comm = list(map(int,input().split()))
    if len(comm) == 3:
        n,i,x = comm[0],comm[1],comm[2]
    else:
        n,i,x = comm[0],comm[1],0
    
    command(n,i-1,x)

answer = 0

for i in range(N):
    if arr[i] not in visited:
        visited.append(arr[i])
        answer += 1

print(answer)