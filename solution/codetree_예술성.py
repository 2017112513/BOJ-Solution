def is_inner(a,b): # 새로운 좌표가 격자를 벗어나는지 판별
    if 0<=a<N and 0<=b<N:
        return True
    return False


def search_group():  # 각 색 별로 그룹을 찾는 함수 
    from collections import defaultdict 
    from copy import deepcopy
    index = 1 
    visited = [[0]*N for _ in range(N)]
    index_count = [0]
    transform = defaultdict(int)
    copy_arr = deepcopy(arr)

    def bfs(i,j):

        cnt = 1
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        from collections import deque
        d = deque()
        visited[i][j] = 1
        d.append((i,j))
        number = arr[i][j]
        transform[index] = arr[i][j] 

        arr[i][j] = index
        
        while d:
            x,y = d.popleft()
            for k in range(4):
                a,b = x+dx[k],y+dy[k]
                if is_inner(a,b) and visited[a][b] == 0 and arr[a][b] == number:
                    visited[a][b] = 1
                    cnt += 1
                    arr[a][b] = index
                    d.append((a,b))
        return cnt 

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                count = bfs(i,j)
                index_count.append(count)
                index+=1 

    return copy_arr, index_count,transform

def calculate_collaborate_score():

    from collections import defaultdict
    dic = defaultdict(int)
    score = 0 
    def bfs(score,i,j):


        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        from collections import deque
        d = deque()
        visited[i][j] = 1
        d.append((i,j))
        number = arr[i][j]
        while d:
            x,y = d.popleft()
            for k in range(4):
                a,b = x+dx[k],y+dy[k]
                if is_inner(a,b) and visited[a][b] == 0:
                    
                    if number == arr[a][b]:
                        visited[a][b] = 1
                        d.append((a,b))
                    else:

                        temp = (index_count[number]+index_count[arr[a][b]])*transform[arr[a][b]]*transform[number]

                        score  = score + temp
        
        return score
                            


    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                score = bfs(score,i,j)

        
    return score


def rotate_reverse(i1,i2,j1,j2):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(i1,i2): # x
        for j in range(j1,j2): # y

            new_arr[N-1-j][i] = arr[i][j]
            
    return new_arr

def rotate(new_arr,i1,i2,j1,j2):
    
    term = N//2-1

    temp_arr = [[0]*N for _ in range(N)]
    temp_arr2 = [[0]*N for _ in range(N)]

    for i in range(0,N//2):
        for j in range(0,N//2):
            temp_arr[i][j] = arr[i1+i][j1+j]

    for _ in range(3):
        for i in range(0,N//2): # x
            for j in range(0,N//2): # y
                temp_arr2[term-j][i] = temp_arr[i][j]

        for i in range(0,N//2):
            for j in range(0,N//2):
                temp_arr[i][j] = temp_arr2[i][j]
    
    for i in range(0,N//2):
        for j in range(0,N//2):
            new_arr[i1+i][j1+j] = temp_arr2[i][j]

    return new_arr


def roll():
   

    new_arr = rotate_reverse(0,N,0,N)
    
    new_arr = rotate(new_arr,0,N//2,0,N//2) # 1
    new_arr = rotate(new_arr,N//2+1,N,0,N//2) # 2
    new_arr = rotate(new_arr,0,N//2,N//2+1,N) # 3 
    new_arr = rotate(new_arr,N//2+1,N,N//2+1,N)# 4
    
    return new_arr    




def main():

    return 


if __name__ == "__main__":

    N=int(input())
    answer = 0
    arr = [list(map(int,input().split())) for _ in range(N)]
    for _ in range(4):
        copy_arr,index_count,transform = search_group()
        score = calculate_collaborate_score()
        answer+=score

        arr = copy_arr
        arr = roll()
    
        
    print(answer)



    
    
    # main()
