def bfs(n,array):
    global answer
    flag = True
    visited = [[0] * n for _ in range(n)]
    d = deque()
    d.append([0,0])
    start = array[0][0]
    while d:

        x,y = d.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<n and not visited[a][b]: 
                visited[a][b] = 1
                if array[a][b] != start:
                    flag = False
                    break
                else:
                    d.append([a,b])
        
        if not flag: 
            answer+='('
            for p in range(0,n,n//2):
                for q in range(0,n,n//2):
                    new_array = []
                    for k in range(0,n//2,1):
                        # print(p,q,k,n)
                        lis = array[p+k][q:q+n//2]
                        new_array.append(lis)
                    
                    bfs(n//2,new_array)
            answer+=')'
            break
    if flag: 
        answer += start

import sys
from collections import deque
input =  sys.stdin.readline
n =  int(input())
arr = [list(input().strip()) for _ in range(n)]
print(arr)

answer=''

dx=[1,-1,0,0]
dy=[0,0,1,-1]

            
bfs(n,arr)
                
print(answer)





# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011