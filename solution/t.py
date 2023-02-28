from collections import deque 
# 도형 내부이면, 그 도형 기준으로 4 방향 탐색해서 빈칸 있으면 갈 수 있고 아니면 완전 내부임; 

def pass_condition(x,y,N,arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    
    count = 0
    
    for i in range(4):
        a,b = x+dx[i],y+dy[i]
        if 0<=a<N and 0<=b<N:
            if arr[a][b] == 0 :
                count += 1
            
        else:
            count+=1
            
    return count
            
def bfs(characterX, characterY, itemX, itemY, N, arr):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    d = deque()
    d.append((0,characterX,characterY))
    
    visited = [[0]*N for _ in range(N)]
    
    visited[characterX][characterY] = 1 
    
    while d:
        count , x , y = d.popleft()
        print(count)
        if [x,y] == [itemX,itemY]:
            return count
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<N and arr[a][b] == 1 and visited[a][b] == 0:
                visited[a][b] = 1

                temp = pass_condition(a,b,N,arr)
                d.append((count+temp,a,b))
    
                
                
            
        
        
    

        
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    max_N = 0 
    for rec in rectangle:
        max_N = max(max_N, rec[2], rec[3])
    
    arr = [[0]*max_N for _ in range(max_N)]
    
    for rec in rectangle:
        for x in range(rec[0],rec[2]):
            for y in range(rec[1],rec[3]):
                arr[x][y] = 1
    for z in arr:
        print(z)
    answer = bfs(characterX, characterY, itemX, itemY, max_N, arr)
    
        
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]] 
characterX, characterY, itemX, itemY= 1,3,7,8
an = solution(rectangle, characterX, characterY, itemX, itemY)

print(an)
