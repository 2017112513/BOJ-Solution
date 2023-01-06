def bfs(l):

    global visited

    visited[','.join(l)] = 1
    temp_visited = [0]*(N+1)
    d = deque()
    d.append(int(l[0])) #리스트의 원소 값은 문자형이므로 변환해서 넣어줌 

    for i in range(1,N+1): # 어떤 노드를 지나가야 하는지 표시 , temp_visited[i]가 1이면 i를 꼭 지나가야 한다는 뜻 
        if str(i) in l:
            temp_visited[i] = 1

    temp_visited[int(l[0])] = 0

    cnt = len(l)
    temp = 1

    while d:
        x = d.popleft()
 
        for next_node in connect[x]:
            if temp_visited[next_node] == 1: #지나가야 하는 노드라면 지나가기
                temp_visited[next_node] = 0 
                temp+=1 
                d.append(next_node)

        if temp == cnt:  # 종료 조건 
            return True

    return False

            


import sys
from collections import deque , defaultdict 
from itertools import combinations

if __name__ == '__main__' : 
    input = sys.stdin.readline
    #--------------------------------------- 초기 세팅 -------------------------------
    N =int(input())
    pop = {str(idx+1) : i for idx,i in enumerate(map(int,input().split()))} # 인구 수 

    connect = defaultdict(list) # 간선 
    visited = defaultdict(int) # 방문
    answer = float(10**9)

    for idx in range(1,N+1):
        temp = list(map(int,input().split()))

        if temp[0] == 0: # 간선이 없으므로 continue
            continue

        n = temp[0]
        for i in range(1,n+1): 
            connect[idx].append(temp[i])
    #--------------------------------------- 초기 세팅 -------------------------------

    lis = list(map(str,range(1,N+1))) # visited에 key값으로 넣어줄 것이기 때문에, string 형으로 받아줌 
    answer_flag = True
    for i in range(1,(N//2)+1): # (3,2)<->(2,3) 의 경우가 나오지 않기 위해 N//2까지만 

        c_list = list(combinations( lis , i )) # 도시를 두 그룹으로 나눌 수 있는 모든 경우를 구하기 위해 조합 

        for c1 in c_list:
            c1 = list(c1) # tuple -> list
            c2 = [i for i in lis if i not in c1] # 전체에서 c1 도시를 빼야 두 그룹으로 나뉘어짐 
        
            if visited[','.join(c1)] == 0: # 리스트를 키값으로 한 Visited,  방문처리를 통해 중복 BFS 방지  , C1이 방문했으면 C2도 방문처리 된것이기 떄문에 
                
                flag1,flag2 = bfs(c1),bfs(c2) #두 그룹 모두 이어진 길이라면. True 출력
            
            if flag1 and flag2:

                answer_flag = False # False면 두 그룹으로 나뉠 수 있는 경우가 존재한다는 의미 
                print(c1,c2,connect)
                sum1,sum2 = sum([pop[i] for i in c1]) , sum([pop[i] for i in c2])
          
                answer = min(abs(sum1-sum2),answer)

    if not answer_flag:
        print(answer)
    else:
        print(-1)
