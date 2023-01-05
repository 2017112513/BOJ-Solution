def is_inner(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def bfs():
    d = deque()
    temp = defaultdict(list) # 작은 바이러스부터 큐에 담기 위해 만든 변수 

    ##########################################
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                temp[arr[i][j]].append((i,j))
    
    for key in sorted(temp.keys()):
        for value in temp[key]:
            d.append((0,value))
    ##########################################

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
   
    while d:
        time,lis = d.popleft()
        
        x,y = lis[0],lis[1]

        if time > S:
            return 0 

        elif time == S:
            for z in arr:
                print(z)
            return arr[X-1][Y-1]

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and arr[a][b] == 0:
                arr[a][b] = arr[x][y]
                d.append((time+1,(a,b)))

    return arr[X-1][Y-1]


if __name__== '__main__':
    import sys
    from collections import deque,defaultdict

    input = sys.stdin.readline

    N,K = map(int,input().split())
    
    arr = [list(map(int,input().split())) for _ in range(N)]

    S,X,Y = map(int,input().split())

    answer = bfs()

    print(answer)
