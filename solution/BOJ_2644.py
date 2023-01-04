
def dfs(cnt,x):

    global visited
    
    visited[x] = cnt

    for next_x in dic[x]:

        if visited[next_x] != 0:
            continue
        else: 
            visited[next_x] = cnt+1
            dfs(cnt+1,next_x)

    
if __name__ == '__main__':
    
    import sys
    from collections import defaultdict    

    input = sys.stdin.readline

    N = int(input()) # 전체 인원 수 
    c1,c2 = map(int,input().split()) # 2인 비교 
    
    m = int(input()) 
    
    dic = defaultdict(list)
    visited = [0] * (N+1)
    for _ in range(m):
        
        x,y = map(int,input().split())
        dic[x].append(y)
        dic[y].append(x)
  
    dfs(0,c1)

    print(visited[c2] if visited[c2] else -1)

    
