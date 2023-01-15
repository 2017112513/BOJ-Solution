def is_inner(x,y):
    if 0<=x<3 and 0<=y<3:
        return True
    return False

def list_to_string(array): 
    return ''.join(sum(array,[]))


def solution(arr,target):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '0':
                x,y = i,j

    d = deque()
    key = list_to_string(arr)
    d.append((0,x,y,key))
    
    visited = defaultdict(int)
    visited[key] = 1
    while d:
        
        cnt, x, y, key = d.popleft()
        arr = [] 
        lis = []
        for i in range(9):
            if i != 0 and i % 3 == 0:
                arr.append(lis)
                lis = []
            
            lis.append(key[i])
        arr.append(lis)

        if arr == target:
            return cnt 

        for i in range(4):
            a,b  = x+dx[i],y+dy[i]
            
            if is_inner(a,b):
                temp = deepcopy(arr)
            
            
                temp[x][y] = arr[a][b]
                temp[a][b] = '0'
                
                key = list_to_string(temp)
                
                if visited[key] == 0:
                    visited[key] = 1

                    d.append((cnt+1,a,b,key))
    return -1
        
        

if __name__ == '__main__':
    
    import sys 
    from collections import deque,defaultdict
    from copy import deepcopy

    target = [['1','2','3'],['4','5','6'],['7','8','0']]

    input = sys.stdin.readline 

    arr = [list(input().split()) for _ in range(3)]

    answer = solution(arr,target)

    print(answer)
