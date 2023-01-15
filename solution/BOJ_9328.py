def list_to_string(x,y,arr):
    return ''.join(arr) + str(x) + str(y)

def is_inner(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def find():# 출입구(벽x)을 찾는 함수 
    find_list = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '.':
                if (i==0 or i == N-1) or (j == 0 or j == M-1):                     
                    find_list.append((i,j))                
    return find_list

def bfs(find_list,key_list):  #탐색하는 함수 
    answer = 0 

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    keys = defaultdict(int)
    d= deque()
    visited = defaultdict(int)

    for k in key_list: 
        keys[k] = 1
    for i,j in find_list: 
        d.append((0,i,j,keys))
        temp = list_to_string(i,j,keys)

        visited[temp] = 1
    
    while d: 
        cnt,x,y,keys = d.popleft()
        
        answer = max(answer,cnt)

        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            temp = list_to_string(a,b,keys)
            
            if is_inner(a,b) and not visited[temp] and arr[a][b] != '*':

                if arr[a][b] == '.':  #빈 공간일때,
                    visited[temp] = 1
                    d.append((cnt,a,b,keys))

                elif arr[a][b].isupper(): # 문일떄,   
                    if keys[arr[a][b].lower()]:
                        print(a,b)
                        visited[temp] = 1
                        d.append((cnt,a,b,keys))
                elif arr[a][b].islower():
                    copy_keys = deepcopy(keys)
                    copy_keys[arr[a][b]] = 1
                    temp =list_to_string(a,b,copy_keys)
                    visited[temp] = 1
                    d.append((cnt,a,b,copy_keys))

                elif arr[a][b] == '$': # 문서일때 
                    visited[temp] = 1
                    d.append((cnt+1,a,b,keys))

    return answer
        

if __name__ == '__main__':
    
    import sys
    from collections import deque,defaultdict
    from copy import deepcopy 

    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        arr = [list(input().strip()) for _ in range(N)]
        find_list = find()

        key_list = list(input().strip()) 
        if key_list[0] == '0':
            key_list = []

        answer = bfs(find_list,key_list)

        print('answer',answer)

    