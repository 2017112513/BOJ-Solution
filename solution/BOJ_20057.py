
def get_new_xy(x,y,dir):

    if dir == 0:
        return x,y-1
    elif dir == 1:
        return x+1,y
    elif dir == 2:
        return x,y+1
    else:
        return x-1,y

def next_direction(dir):
    if dir%4 == 3:
        return 0
    else:
        return (dir%4)+1

def after_sand(x,y,dir,sand):
    global answer
    ds = [0.02,0.1,0.07,0.01,0.05,0.1,0.07,0.01,0.02]

    if dir==0:
        dx = [-2,-1,-1,-1,0,1,1,1,2]
        dy = [0,-1,0,1,-2,-1,0,1,0]
    elif dir == 1:
        dx = [0,1,0,-1,2,1,0,-1,0]
        dy = [-2,-1,-1,-1,0,1,1,1,2]
    elif dir == 2:
        dx = [2,1,1,1,0,-1,-1,-1,-2]
        dy = [0,1,0,-1,2,1,0,-1,0]
    else:
        dx = [0,-1,0,1,-2,-1,0,1,0]
        dy = [2,1,1,1,0,-1,-1,-1,-2]

    temp = 0
    for i in range(9):
        new_x,new_y = x+dx[i],y+dy[i]
        
        if 0<=new_x<N and 0<=new_y<N:
            # print(i,int(sand*ds[i]))
            arr[new_x][new_y] += int(sand*ds[i])
        else:
            answer += int(sand*ds[i])

        temp+=int(sand*ds[i])

    a,b = get_new_xy(x,y,dir)

    if 0<=a<N and 0<=b<N:
        plus_a = sand-temp
        arr[a][b] += plus_a
    else:
        plus_a = sand-temp
        answer+=plus_a

def bfs(dir,x,y,roll_weight):
    
    for _ in range(dis):

        x,y = get_new_xy(x,y,dir)
        if 0<=x<N and 0<=y<N:
            if arr[x][y]:
                sand = arr[x][y]
                after_sand(x,y,dir,sand)
                arr[x][y] = 0
        
        if x == 0 and y == 0:
            return 1,1,1,dir,answer
    roll_weight += 1

    new_dir = next_direction(dir)
    return x,y,roll_weight,new_dir,False



import sys
input = sys.stdin.readline

N = int(input())
answer = 0
arr = [list(map(int,input().split())) for _ in range(N)]

x,y = N//2,N//2 

dir = 0
dis = 1  # dis만큼 바람이 부는 방향으로 움직일 것이다
roll_weight = 0 # 짝수가 되면 dis가 +1 증가한다 

while 1:
    x,y,roll_weight,dir,flag = bfs(dir,x,y,roll_weight)
    if flag != False:
        print(flag)
        break
    if roll_weight%2 == 0:
        dis+=1
    

