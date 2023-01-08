def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def search():

    global visited 
    d = deque()
    water = deque()
    for i in range(N):
        for j in range(M):

            if arr[i][j] == 'S':
                d.append((i,j))
            elif arr[i][j] == '*':
                water.append((i,j))
                visited[i][j] = 1
    return d,water

        
def bfs_water(water):
    
    global visited
    new_water = deque()

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    
    while water :
        x,y = water.popleft()

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and visited[a][b] == 0 and arr[a][b] != 'D' and arr[a][b] !='X':
                visited[a][b] = 1
                new_water.append((a,b))

    return new_water

def bfs_kak(d):
    global visited
    new_d = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    flag = False

    while d:
        x,y = d.popleft()
        if arr[x][y] == 'D':
            flag = True
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and visited[a][b] == 0 and arr[a][b] != '*' and arr[a][b] !='X':
                visited[a][b] = 1
                new_d.append((a,b))
    return flag, new_d

if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline    

    N,M = map(int,input().split())
    arr = [list(input().strip()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    
    
    d,water = search()

    answer = 0
    while True:

        

        water = bfs_water(water)
        flag , d = bfs_kak(d)
        answer+=1 

        if flag:
            print(answer-1)
            break
        elif not flag and not d:
            print('KAKTUS')
            break

        
        
        

    