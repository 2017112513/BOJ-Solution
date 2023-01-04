def is_inner(x,y):
    if 0<=x<N and 0<=y<M and not visited[x][y] and not arr[x][y]:
        return True
    return False
def bfs(x,y):
    global visited 

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = 1
    
    d = deque()
    d.append((x,y))
    
    hap = 1
    while d:
        x,y = d.popleft()
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b):
                visited[a][b] = 1
                hap+=1
                d.append((a,b))
    return hap
        




if __name__ =='__main__':
    
    import sys
    from collections import deque

    input = sys.stdin.readline
    
    N,M,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer_list = []

    for _ in range(K):
        
        x1,y1,x2,y2 = map(int,input().split())
        for x in range(y1,y1+abs(y2-y1)):
            for y in range(x1,x1+abs(x1-x2)):
                arr[x][y] = 1


    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:

                hap = bfs(i,j)
                answer_list.append(hap)  
    
    print(len(answer_list))
    print(*sorted(answer_list))
                
    
    