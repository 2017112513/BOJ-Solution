def H(d,x,cnt,iter,visited,answer_dic):

    if iter == 0:

        if visited[x-1] == 0:
            if x-1 >= 0 :
                visited[x-1] = cnt+1
                d.append((cnt+1,x-1))
            if x-1 == brother:
                answer_dic[cnt+1] += 1
        else: 
            if x-1 == brother:
                # print(brother,0)
                if cnt + 1 < visited[x-1]:
                    visited[x-1] = cnt + 1
                    answer_dic[cnt+1] += 1 
                elif cnt + 1 == visited[x-1]:
                    answer_dic[cnt+1] += 1
            
            else:
                if cnt + 1 < visited[x-1]:
                    visited[x-1] = cnt + 1
           
                    d.append((cnt+1,x-1))

                elif cnt + 1 == visited[x-1]:
              
                    d.append((cnt+1,x-1))

    elif iter == 1:

        if visited[x+1] == 0:
            visited[x+1] = cnt+1
            d.append((cnt+1,x+1))
            if x+1 == brother:
                answer_dic[cnt+1] += 1
        else: 
            if x+1 == brother:
                # print(brother,1)
                if cnt + 1 < visited[x+1]:
                    visited[x+1] = cnt + 1
                    answer_dic[cnt+1] += 1 

                elif cnt + 1 == visited[x+1]:
                    answer_dic[cnt+1] += 1

            else:
                if cnt + 1 < visited[x+1]:
                    visited[x+1] = cnt + 1
               
                    d.append((cnt+1,x+1))

                elif cnt + 1 == visited[x+1]:
              
                    d.append((cnt+1,x+1))

    else:
        if visited[x*2] == 0:
            if x*2 == brother:
                answer_dic[cnt+1] += 1
         
            visited[x*2] = cnt+1
            d.append((cnt+1,x*2))

        else: 
            if x*2 == brother:
         
                if cnt + 1 < visited[x*2]:
                    visited[x*2] = cnt + 1
                    answer_dic[cnt+1] += 1 
          

                elif cnt + 1 == visited[x*2]:
                    answer_dic[cnt+1] += 1

            else:
                if cnt + 1 < visited[x*2]:
                    visited[x*2] = cnt + 1
       
                    d.append((cnt+1,x*2))

                elif cnt + 1 == visited[x*2]:
    
                    d.append((cnt+1,x*2))

    return d,visited,answer_dic
        

def bfs():
    
    visited = defaultdict(int)
    
    d = deque()
    d.append((0,subin))
    visited[subin] = 1

    answer_dic = defaultdict(int)
    
    while d:
        cnt , x = d.popleft()


        if x> 100000:
            continue
        
        for iter in range(3):
   
            d , visited, answer_dic= H(d,x,cnt,iter,visited,answer_dic)
          
        
    return answer_dic

import sys
from collections import deque, defaultdict
input = sys.stdin.readline


if __name__ == '__main__':
    
    subin, brother = map(int,input().split()) 
    
    if subin == brother:
        print(0)
        print(1)
    else:
        answer = bfs()
 
        key = min(answer)
        
        print(key)
        print(answer[key])