def locations():
    d = deque()
    sanguen_q = deque()
    visited = [[0]*M for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                sanguen_q.append((i,j))
                arr[i][j] = '.'
                if (i == 0 or j == 0) or (i== N-1 or j== M-1 ):
                    flag = False

            elif arr[i][j] == '*':
                d.append((i,j)) # x, y
                visited[i][j] = 1

    return d,sanguen_q,visited,flag


def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False


def bfs_fire(d,visited):

    temp_q = deque()

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while d:
        
        x,y = d.popleft()

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and visited[a][b] != 1 and arr[a][b]== '.' :
                visited[a][b] = 1
                temp_q.append((a,b))
    
    return temp_q,visited

def bfs_me(d,visited):

    flag = True

    temp_q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while d:

        x,y = d.popleft()
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and visited[a][b]== 0 and arr[a][b] == '.':
                visited[a][b] = 2

                temp_q.append((a,b))

                if (a==0 or a==N-1) or (b==0 or b==M-1):

                    flag = False
                    break

    return temp_q,flag
    



if __name__ == '__main__':

    import sys
    from collections import  deque 

    input= sys.stdin.readline

    T = int(input())

    answer_list = []
    for _ in range(T):

        M,N  = map(int,input().split())

        arr = [list(input().strip()) for _ in range(N)]

        d,sanguen_q,visited,sg_flag = locations()

        answer = 0

        while True:
            if not sg_flag:
                print(1)
                break

            d,visited= bfs_fire(d,visited)

            sanguen_q,flag = bfs_me(sanguen_q,visited)

            answer+=1 

            
            if not flag:
                answer_list.append(answer+1)
                break
            
            if not sanguen_q:
                answer_list.append("IMPOSSIBLE")
                break
    for i in answer_list:
        print(i)