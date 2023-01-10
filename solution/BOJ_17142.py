def get_virus():

    virus = [] 

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                virus.append([i,j])
    return virus 

def is_inner(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
    

def bfs(d,is_virus):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    day = 0
    while d:
        curr_day,x,y = d.popleft()
        # print(curr_day,x,y)   
        day = max(day,curr_day)

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if is_inner(a,b) and not is_virus[str(a)+','+str(b)]:
                if arr[a][b] == 0:
                    is_virus[str(a)+','+str(b)] = 1
                    d.append((curr_day+1,a,b))
                elif arr[a][b] == 2:
                    is_virus[str(a)+','+str(b)] = 1
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and is_virus[str(i)+','+str(j)] == 0:
                return -1

    return curr_day

if __name__ == '__main__':
    import sys
    from collections import deque,defaultdict
    from itertools import combinations

    input = sys.stdin.readline

    N,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    virus = get_virus()

    c_list = list(combinations(virus,K))

    

    INF = 10**9
    ans = INF
    flag = True

    for c in c_list:
        d = deque()
        is_virus = defaultdict(int)
        for i,j in c:
            
            d.append((0,i,j))
            is_virus[str(i)+','+str(j)] = 1
        # print(c)
        answer = bfs(d,is_virus)
  
        if answer != -1:
            if flag:
                ans = answer
                flag = False
            else:
                ans = min(answer,ans)
            print(answer,ans)
        elif answer == -1:
            if flag:
                ans = -1 
        

    print(ans)





    

