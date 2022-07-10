def search_feed(sx,sy):
    print('sxsy',sx,sy)
    feed = []
    visited = [[0]*N for _ in range(N)]
    d = deque()
    d.append([0,sx,sy])
    visited[sx][sy] = 1
    while d:
        for _ in range(len(d)):
            dis,x,y = d.popleft()

            for i in range(4):
                a = x+dx[i]
                b = y+dy[i]
                
                if 0<=a<N and 0<=b<N and not visited[a][b] and graph[a][b]<=level:
                    if 0<graph[a][b]<level:
                        visited[a][b] = 1
                        feed.append([dis+1,a,b])
        
                    else:
                        visited[a][b] = 1
                        d.append([dis+1,a,b])
        if feed:
            feed = sorted(feed,key=lambda x : (-x[1],-x[2]))
            print(feed)
            distance,target_x,target_y = feed.pop()
            return distance,target_x,target_y
    return 0,0,0





from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
level = 2
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if graph[i][j] ==9:
            graph[i][j] = 0
            shark_x,shark_y = i,j
answer = 0




get_feed = 0
while True:
    # print(feed)
    distance,target_x,target_y = search_feed(shark_x,shark_y)
    print(distance,target_x,target_y)
    if distance == 0:
        break

    answer += distance
    get_feed += 1
    graph[target_x][target_y] = 0
    if get_feed == level:
        level+=1 
        get_feed = 0
    shark_x,shark_y = target_x,target_y


print(answer)


        

