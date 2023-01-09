def bfs(i):

    d = deque()

    d.append(i)
    
    visited[i] = 1
    
    while d:
        x = d.popleft()
        for next_x in dic[x]:
            if  visited[next_x] == 0:
                visited[next_x] = -1 * visited[x]
                d.append(next_x)

            else:
                if visited[next_x] == visited[x]:
                    return True # 이분 그래프 X
    return False # 이분 그래프 

 
if __name__ == '__main__':
    import sys
    from collections import deque, defaultdict
    input = sys.stdin.readline
    

    T = int(input())

    for _ in range(T):
        answer_flag = True
        V,E = map(int,input().split())
        visited = [0]*(V+1)
        dic = defaultdict(list)
        for _ in range(E):
            a,b = map(int,input().split())
            dic[a].append(b)
            dic[b].append(a)

        for i in range(1,V+1):
            if visited[i] == 0:
                if bfs(i):
                    answer_flag = False
                    print('NO')
                    break
                    
        if  answer_flag:        
            print('YES')