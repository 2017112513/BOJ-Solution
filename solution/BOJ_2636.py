def search_cheese():

    flag = True
    
    d = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                d.append((i,j))
                flag = False

    return flag,d

def is_inner(x,y):
    if 0<=x<N and 0<=y<M :
        return True
    return False

def bfs(d):


    def cheese(x,y):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        d = deque()
        visited= [[0]*M for _ in range(N)]

        d.append((x,y))
        visited[x][y] = 1

        while d:
            x,y = d.popleft()
            for i in range(4):
                a,b = x+dx[i],y+dy[i]
                if is_inner(a,b) and visited[a][b] == 0 and arr[a][b] == 0:
                    visited[a][b] = 1
                    d.append((a,b))
                elif not is_inner(a,b):
                    return True
        return False


    global answer_cnt

    air_list =[]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    answer_cnt = len(d)

    while d:

        x,y = d.popleft()

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and arr[a][b] == 0 and cheese(a,b):
         
                air_list.append((x,y))
                break
            elif not is_inner(a,b):
                air_list.append((x,y))
                break
                
    
    return air_list




if __name__ == '__main__':
    import sys
    from collections import deque

    answer_time = 0
    answer_cnt = 0

    input = sys.stdin.readline
    
    N,M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    while True:


        
        flag , d = search_cheese()

        if not flag:
            answer_time += 1
            air_list = bfs(d)

            while air_list:
                x,y = air_list.pop()
                arr[x][y] = 0



        else:
            print(answer_time)
            print(answer_cnt)
            break


    

        
