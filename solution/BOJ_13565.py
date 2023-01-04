

def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def yes_or_no(a,b):
    if a == N-1:
        return True
    return False

def bfs(x,y):
    global visited 

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    d.append((x,y))
    visited[x][y] = 1

    while d:
        x,y = d.popleft()
        
        if yes_or_no(x,y):
    
            return True
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not visited[a][b] and arr[a][b] == 0:
                visited[a][b] = 1
                d.append((a,b))
        
    return False
    

    return 
if __name__ == '__main__':
    import sys
    from collections import deque 

    input = sys.stdin.readline

    N,M = map(int,input().split()) 

    arr = [list(map(int,list(input().strip()))) for i in range(N)]  # 0: 흰색 , 1 : 검정색 
    
    w_list = [] 

    for i in range(M):
        if arr[0][i] == 0:
            w_list.append((0,i))
    visited = [[0]*M for _ in range(N)]

    flag = False
    for x,y in w_list:
        if not visited[x][y]:
            answer = bfs(x,y)
            if answer:
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")
    

    

    