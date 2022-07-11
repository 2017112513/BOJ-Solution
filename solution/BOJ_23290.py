

def next_dir(n):
    if n==1:
        return 8
    else:
        return n-1

def fix_next_xy(n,x,y):
    new_direction = n
    flag = True
    cnt=0
    while flag:
        if cnt == 8:
            return x,y,n
        next_x,next_y = x+dx[n] , y+dy[n]
        if  [next_x,next_y] != [sx,sy] and 0<=next_x<4 and 0<=next_y<4 and not visited[next_x][next_y]:
            flag = False
            return next_x,next_y,new_direction
        else:
            new_direction = next_dir(n)
            n = new_direction
            
        cnt+=1
    


def direction_to_number(lis):
    answer = ''
    for i in lis:
        if i == [-1,0]:
            answer+='1'
        elif i==[0,-1]:
            answer+='2'
        elif i==[1,0]:
            answer+='3'
        else:
            answer+='4'
    return int(answer)

def next_shark_xy():
    get_fish = []
  
    for ds in d_shark:
        temp_x,temp_y = sx,sy
        cnt = 0
        move_fish_lis = []

        for i,j in ds:
            a = temp_x+i
            b = temp_y+j
            if  0<=a<4 and 0<=b<4:
                if [a,b] not in move_fish_lis:
                    cnt += arr[a][b]
                else:
                    pass
                temp_x,temp_y = a,b
                move_fish_lis.append([a,b])

            else:
                break
        
        if len(move_fish_lis) == 3:
            # print(cnt,move_fish_lis)
            get_fish.append([cnt,direction_to_number(ds),move_fish_lis])
    
    get_fish = sorted(get_fish,key=lambda x: (-x[0],x[1]))
    # print(get_fish)
    return get_fish[0]

#############################################
from itertools import product
from copy import deepcopy
import sys
input = sys.stdin.readline

N,S = map(int,input().split())

dx = [0,0,-1,-1,-1,0,1,1,1] # 1~8에서 방향이 정해짐
dy = [0,-1,-1,0,1,1,1,0,-1]
d_shark_list = [[1,0],[-1,0],[0,-1],[0,1]]



fish = []

for _ in range(N):
    nx,ny,nd = map(int,input().split())
    fish.append([nx-1,ny-1,nd])

sx,sy = map(int,input().split())
sx,sy = sx-1,sy-1
d_shark = list(product(d_shark_list,repeat = 3))
visited = [[0]*4 for _ in range(4)]


for s in range(S):
    
    next_dir_list = [[0] * 4 for _ in range(4)]
    
    arr = [[0] * 4 for _ in range(4)]

    for i,j,d in fish:
        arr[i][j] += 1 # 물고기 존재

    
    next_fish_list = []
    for k in range(len(fish)):
        x,y,direction = fish[k]
        
        next_x,next_y,next_direction = fix_next_xy(direction,x,y)
        # print(x,y,direction,'->',next_x,next_y,next_direction)
        arr[x][y] -= 1 
        arr[next_x][next_y] += 1
        
        next_fish_list.append([next_x,next_y,next_direction])
    # print('복제 후 방향 바꾸고 이동한 후 물고기 ')
    # for A in arr:
    #     print(A)

    # print('vis')
    # for v in visited:
    #     print(v)
    
    get_fish_cnt,_,move_fish_list = next_shark_xy()
    next_sx,next_sy = move_fish_list[2][0] ,move_fish_list[2][1] 



    for i in range(4):
        for j in range(4):
            if visited[i][j] != 0:
                visited[i][j] -= 1

    sx,sy = next_sx,next_sy
    # print('움직임 후 위치 ',sx,sy,get_fish_cnt)
    new_fish_list = []
    smell_list = []
    
    for i,j,d in next_fish_list:
        if [i,j] not in move_fish_list:
            new_fish_list.append([i,j,d])
        else:
            visited[i][j] =2

    for f in fish:
        new_fish_list.append(f)
    fish = new_fish_list

print(len(fish))

        
