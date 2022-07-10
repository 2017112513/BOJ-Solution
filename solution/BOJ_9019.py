def func(x,n,string):
    if x == 0: # 
        string += 'D'
        n = str((2*int(n))%10000)
        if len(n)== 1:
            n = '000'+n
        elif len(n) == 2:
            n ='00'+n
        elif len(n) == 3:
            n = '0'+n
   
        return n,string

    elif x== 1: # S
        string += 'S'
        if n == '0000':
            return '9999',string
        else:
            n = str(int(n)-1)
            N = len(n)
        
            if N== 1:
                n = '000'+n
            elif N == 2:
                n ='00'+n
            elif N == 3:
                n = '0'+n
        

            return n,string

    elif x == 2: # L 
        string += 'L'
        a,b = n[0],n[1:]
        n = b+a

        return n,string
                    
    else: # R
        string += 'R'
        a,b = n[0:2+1],n[3]
        n = b+a

        return n,string

def bfs(n):
    answer = ''
    d = deque()
    d.append([n,answer])
    visited[int(n)] = 1
    
    while d:
        x,strg = d.popleft()
        # print(x,strg)

        if x == m:
            return strg

        for i in range(4):
            new_x,new_string = func(i,x,strg)
            if not visited[int(new_x)]:
                visited[int(new_x)]=1
                d.append([new_x,new_string])

def arange(N):
    if len(N) == 1:
        N = '000'+N
    elif len(N) == 2:
        N = '00'+N
    elif len(N) == 3:
        N = '0'+N
    return N



from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    
    n,m = input().rstrip().split()
    n,m = arange(n),arange(m)
    visited = [0]*(10000+1)    

    ans = bfs(n)
    print(ans)


