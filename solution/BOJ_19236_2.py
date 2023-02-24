import sys
from collections import deque, defaultdict

def next_direction(dir):
    
    if dir >= 8:
        return 1
    return dir + 1

def next_location(dir,x,y,sx,sy):
    dx = [99,-1,-1,0,1,1,1,0,-1] # index가 1부터 시작하도록 맞춰주기 위해 맨 앞에 99추가
    dy = [99,0,-1,-1,-1,0,1,1,1]
    
    visited = [0]*(8+1)
    while True:
        a,b = x+dx[dir],y+dy[dir]
        # print(x,y,dir,a,b)
        if 0<=a<4 and 0<=b<4 and ([a,b]!=[sx,sy]):#(a!=sx and b!=sy)
            return a,b,dir
        else:
            if visited[dir] == 1:
                return x,y,dir
            visited[dir] = 1
            
            dir = next_direction(dir)


            

def fish_move(fish_dic,arr,sx,sy):
    
    fish_sorted_num = sorted([key for key,value in fish_dic.items() if value],reverse=True)

    while fish_sorted_num:

        fish_num = fish_sorted_num.pop()

        x,y,dir = fish_dic[fish_num]

        a,b,new_dir= next_location(dir,x,y,sx,sy)

        if fish_dic[arr[a][b]]:
            
            temp_x,temp_y,temp_dir = fish_dic[arr[a][b]] 

            fish_dic[arr[a][b]] = (x,y,temp_dir)
            fish_dic[fish_num] = (a,b,new_dir)

            arr[x][y] = arr[a][b]
            arr[a][b] = fish_num
            
        else:
            fish_dic[arr[a][b]] = []
            fish_dic[fish_num] = (a,b,new_dir)
            arr[x][y] = 0
            arr[a][b] = fish_num

            

    return fish_dic,arr
        
def shark_next_location(dir,x,y,arr):
    dx = [99,-1,-1,0,1,1,1,0,-1] # index가 1부터 시작하도록 맞춰주기 위해 맨 앞에 99추가
    dy = [99,0,-1,-1,-1,0,1,1,1]

    feed = []
    while True:
        a,b = x+dx[dir],y+dy[dir]


        for i in range(4):
            a,b = x+i*dx[dir],y+i*dy[dir]
            if 0<=a<4 and 0<=b<4 and arr[a][b]!=0:
        
                feed.append(arr[a][b])

        else:
            return feed

def shark_move(fish_dic,arr,s_dir,sx,sy,cnt):
    global d
    from copy import deepcopy

    feed = shark_next_location(s_dir,sx,sy,arr)

    print(sx,sy)
    print(fish_dic)
    for z in arr:
        print(z)
    if not feed:
        return False,0,0

    for feed_num in feed:

        copy_arr = deepcopy(arr)
        copy_fish_dic = deepcopy(fish_dic)
        sx,sy,s_dir = copy_fish_dic[feed_num]
        
        copy_fish_dic[feed_num] = []
        copy_arr[sx][sy] = 0

        d.append((copy_fish_dic,copy_arr,sx,sy,s_dir,cnt+feed_num))

    return True,0,0


if __name__ == '__main__':

    arr = [[0]*4 for _ in range(4)]
    
    fish_dic = defaultdict(list)
    for i in range(4):
        temp = list(map(int,input().split()))
        for j in range(4):
            if i == 0 and j == 0:
                
                sx,sy,s_dir = 0,0,temp[1]
                cnt = temp[0]
                continue
            fish_num , fish_dir = temp[j*2],temp[j*2+1]
             
            arr[i][j] = fish_num
            fish_dic[fish_num]=(i,j,fish_dir) # 물고기의 좌표와 방향 

    answer = []
    d = deque()
    d.append((fish_dic,arr,sx,sy,s_dir,cnt))
    while d:
        print(len(d))
        fish_dic,arr,sx,sy,s_dir,cnt = d.popleft()
 
        fish_dic,arr = fish_move(fish_dic,arr,sx,sy)  
        flag,n,m = shark_move(fish_dic,arr,s_dir,sx,sy,cnt) 

        if not flag:
            answer.append(cnt)

            continue
    print(answer)



