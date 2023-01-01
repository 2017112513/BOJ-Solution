def bfs(answer):
    d = deque()
    d.append(A)
    visited[A] = 1    
    
    while d: # O((len(B)-len(A)) * 2)
        x = d.popleft()

        if len(x)<len(B):  
            for ascii in range(97,122+1):
                if visited[x + chr(ascii)] == 0:
                    visited[x + chr(ascii)] = 1
                    d.append(x + chr(ascii))

                if visited[chr(ascii) + x] == 0:
                    visited[chr(ascii) + x] = 1
                    d.append(chr(ascii) + x)
        else:
            temp = 0
            for a,b in zip(x,B):
                if a != b:
                    temp += 1

            answer = min(answer,temp)

    return answer

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

answer =  float('inf')
visited = defaultdict(int)
A,B = input().split()

answer = bfs(answer)

print(answer)




            
            
            
        

    


