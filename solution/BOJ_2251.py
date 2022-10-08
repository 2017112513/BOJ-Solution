def bfs(): # 내일 다른 방법으로 풀어서 올리고 

    while d:
        new_a,new_b,new_c = d.popleft()
        flag_a,flag_b,flag_c = False,False,False
        
        if new_a<a:
            flag_a = True 
        if new_b<b:
            flag_b = True
        if new_c<c:
            flag_c = True
        
        
        if new_a: # 현재 a에 물이 있으면 
            if flag_b: # 현재 b에 물이 들어갈 공간이 있으면 
                if new_b>=new_a and not visited[0][new_b+new_a][new_c]:
                    d.append(0,new_b+new_a,new_c)
                    visited[0][new_b+new_a][new_c] = 1
                elif new_b<a:
                    if (b-new_b)>=new_a and not visited[0][new_a][new_c]:
                        d.append([0,new_a,new_c])
                        visited[0][new_a][new_c]=1
                    
                    else:
                        if not visited[new_a-(b-new_b)][b][new_c]:
                            visited[new_a-(b-new_b)][b][new_c] = 1
                            d.append([new_a-(b-new_b),b,new_c])

            if flag_c:
                if new_c>=new_a and not visited[0][new_b][new_c+new_a]:
                    d.append(0,new_b,new_c+new_a)
                    visited[0][new_b][new_c+new_a] = 1
                elif new_c<a:
                    if (c-new_c)>=new_a and not visited[0][new_b][new_a]:
                        visited[0][new_b][new_a] = 1
                        d.append([0,new_b,new_a])
                    else:
                        if not visited[new_a-(c-new_c)][new_b][c]:
                            visited[new_a-(c-new_c)][new_b][c] = 1
                            d.append([new_a-(c-new_c),new_b,c])
    


        if new_b:
            if flag_a: # 현재 b에 물이 들어갈 공간이 있으면 
                if new_a>=new_b and not visited[new_b+new_a][0][new_c]:
                    d.append([new_b+new_a,0,new_c])
                    visited[new_b+new_a][0][new_c] = 1
                elif new_a<new_b:
                    if (a-new_a)>=new_b and not visited[new_b][0][new_c]:
                        d.append([new_b,0,new_c])
                        visited[new_b][0][new_c] = 1
                    else:
                        if not visited[a][new_b-(a-new_a)][new_c]:
                            d.append([a,new_b-(a-new_a),new_c])
                            visited[a][new_b-(a-new_a)][new_c] = 1

            if flag_c:
                if new_c>=new_b and not visited[new_a][0][new_c+new_b]:
                    d.append([new_a,0,new_c+new_b])
                    visited[new_a][0][new_c+new_b] = 1
                
                elif new_c<new_b:
                    if (c-new_c)>=new_b and not visited[new_a][0][new_b]:
                        d.append([new_a,0,new_b])
                        visited[new_a][0][new_b] = 1
                    else:
                        if not visited[new_a][new_b-(c-new_c)][c]:
                            d.append([new_a,new_b-(c-new_c),c])
                            visited[new_a][new_b-(c-new_c)][c] = 1


        if new_c:
            if flag_a:
                if new_a>=new_c and not visited[new_a+new_c][new_b][0]:
                    d.append([new_a+new_c,new_b,0])
                    visited[new_a+new_c][new_b][0] = 1
                elif new_a<new_c:
                    if (a-new_a)>=new_c and not visited[new_c][new_b][0]:
                        d.append([new_c,new_b,0])
                        visited[new_c][new_b][0] = 1
                    else:
                        if not visited[a][new_b][new_c-(a-new_a)]:
                            d.append([a,new_b,new_c-(a-new_a)])
                            visited[a][new_b][new_c-(a-new_a)] = 1

            if flag_b:
                if new_b>=new_c and not visited[new_a][new_b+new_c][0]:
                    d.append([new_a,new_b+new_c,0])
                    visited[new_a][new_b+new_c][0] = 1
                elif new_b<new_c:
                    if (b-new_b)>=new_c and not visited[new_a][new_c][0]:
                        d.append([new_a,new_c,0])
                        visited[new_a][new_c][0] = 1
                    else:
                        if not visited[new_a][new_c][new_c-(b-new_b)]:
                            d.append([new_a,b,new_c-(b-new_b)])
                            visited[new_a][b][new_c-(b-new_b)] = 1
import sys
from collections import deque
input = sys.stdin.readline
a,b,c = map(int,input().split())

visited = [[[0]*(10+1) for _ in range(10+1)] for _ in range(10+1)]

answer = []


d = deque()
d.append([0,0,c])
visited[0][0][c] = 1

bfs()


for i in visited[0]:
    for j in i:
        print(j)





            






# if b>=c:
#     answer.append(0)
#     if a<c:
#         answer.append(c-a)
# else:#b<c
#     answer.append(c-b)
#     if a<c:
#         answer.append(c-a)
#     elif a==c:
#         answer.append(0)




# answer = sorted(answer)
# print(answer)
