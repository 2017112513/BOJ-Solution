def is_inner(x1,y1,x2,y2):
    if abs(x1-x2) + abs(y1-y2) <= 1000:
        return True
    return False

def bfs():

    d = deque()
    visited = defaultdict(int)
    visited[str(home_x) + str(home_y)] = 1

    d.append((home_x,home_y,visited))

    while d:
        x,y,vis = d.popleft()
        
        if is_inner(x,y,target_x,target_y):
            return 'happy'

        for s_x,s_y in store_list:
            if is_inner(x,y,s_x,s_y) and not vis[str(s_x)+str(s_y)]:
                vis[str(s_x)+str(s_y)] = 1
                d.append((s_x,s_y,vis))
                
    return 'sad'

    
    

if __name__ == '__main__':
    import sys
    from collections import deque,defaultdict

    input = sys.stdin.readline 
    
    for _ in range(int(input())):
        store_cnt = int(input())
        
        home_x,home_y = map(int,input().split())
        
        store_list = [list(map(int,input().split())) for _ in range(store_cnt)]
                
        target_x,target_y = map(int,input().split())

        answer = bfs()

        print(answer)
    