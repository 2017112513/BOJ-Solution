def get_virus():

    virus = [] 
    zero = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                virus.append([i,j])
            elif arr[i][j] ==0:
                zero += 1
    return virus ,zero

def is_inner(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
    

def bfs(d,copy_arr,visited,cnt):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    day = 0
    while d:
        curr_day,x,y = d.popleft()

        day = max(day,curr_day)

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not visited[a][b] and arr[a][b] != 1:

                if copy_arr[a][b] == 0:
        
                    copy_arr[a][b] = 2
                    visited[a][b] = 1
                    cnt -= 1
                    d.append((curr_day+1,a,b))
                
                elif copy_arr[a][b] == 2:
                    visited[a][b] = 1
                    d.append((curr_day+1,a,b))

                if cnt == 0:
                    return curr_day+1
            

    if cnt>0:
        return -1 


if __name__ == '__main__':
    import sys
    from collections import deque,defaultdict
    from itertools import combinations
    from copy import deepcopy 

    input = sys.stdin.readline

    N,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    virus , zero = get_virus()

    c_list = list(combinations(virus,K))

    

    INF = 10**9
    ans = INF
    flag = True
    if zero == 0:
        print(0)
    else:
        for c in c_list:
            temp_cnt = zero
            d = deque()
            copy_arr = deepcopy(arr)
            visited  = [[0]*N for _ in range(N)]
            
            for i,j in c:
                d.append((0,i,j))
                visited[i][j] = 1
            
            
            answer = bfs(d,copy_arr,visited,temp_cnt)
            # print(answer)

            if answer != -1:
                if flag:
                    ans = answer
                    flag = False
                else:
                    ans = min(answer,ans)
            elif answer == -1:
                if flag:
                    ans = -1 
            

        print(ans)





    

