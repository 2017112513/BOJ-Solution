def bfs(x,y,feed_x,feed_y):
    dis = 0
    visited = [[0]*N for _ in range(N)]
    d = deque()
    d.append([0,x,y])
    visited[x][y] = 1
    while d:
        dis,x,y = d.popleft()
        if x==feed_x and y==feed_y:
            return dis
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N and not visited[a][b] and graph[a][b] != 's' and graph[a][b]<=level:
                visited[a][b] = 1
                d.append([dis+1,a,b])
    return 0

def search_feed(sx,sy):
    feed = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 's' and 0 < graph[i][j] <level:
                distance = bfs(sx,sy,i,j)
                if distance != 0:
                    feed.append([distance,i,j])
    if feed:
        feed = sorted(feed,key=lambda x : (-x[0],-x[1],-x[2]))
    
    return feed



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


feed = search_feed(shark_x,shark_y)


while feed:
    # print(feed)
    distance,target_x,target_y = feed.pop()
    visited = [[0]*N for _ in range(N)]
    d = deque()
    d.append([shark_x,shark_y,0])

    get_feed = 0
    loop_flag = True


    while d:
        x,y,sec = d.popleft()
    
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N and not visited[a][b] and graph[a][b] != 's' and graph[a][b]<=level:
                visited[a][b] = 1
                if a==target_x and b==target_y:
                    
                
                    graph[a][b] = 0
                    get_feed += 1
                    graph[shark_x][shark_y] = 0
                    shark_x,shark_y = a,b
                    graph[a][b] = 9

                    answer += sec+1

                    visited =[[0]*N for _ in range(N)]
                    visited[a][b] = 1
                    
                    if get_feed==level:

                        level+=1
                        get_feed = 0
                        feed = search_feed(shark_x,shark_y)
                        break
                    else:
                        d = deque()
                        d.append([a,b,0])
                        feed = search_feed(shark_x,shark_y)
                        if feed:
                            # print(feed)
                            distance,target_x,target_y = feed.pop()
                            break
                else:
              
                    d.append([a,b,sec+1])
print(answer)
