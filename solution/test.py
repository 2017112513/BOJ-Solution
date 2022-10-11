
# answer = []
# def solution(name):
#     global answer
#     from copy import deepcopy
#     alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     dic = {}

#     for idx, ab in enumerate(alphabet):
#         dic[ab] = idx

#     start_string = 'A'*len(name)
#     dic_visited = {}
    

#     answer = []
#     ud_cnt = 0
#     for idx,lst in enumerate(zip(name,start_string)):
#         i,j = lst[0],lst[1]
        
#         tmp_cnt = min(abs(dic[i]-dic[j]) , abs(len(dic)-abs(dic[i]-dic[j])) )
#         if i!=j:
#             dic_visited[idx]= 0
        
#         ud_cnt+= tmp_cnt
    
#     dic_visited[0] = 1
    
#     def recursion(cnt,idx,vis,name):
        
#         if sum((vis.values()))==len(vis):
      
#             answer.append(cnt)
#             return 
#         else:

#             for i in vis.keys():
                
#                 if vis[i] == 0:
#                     new_vis = deepcopy(vis)
        
#                     new_vis[i] =1 
#                     recursion(cnt+abs(idx-i),i,new_vis,name)
#                     recursion(cnt+abs(idx+len(name)-i ),i,new_vis,name)   
            
        

        
#     recursion(0,0,dic_visited,name)
    
#     ans = ud_cnt+ min(answer)
    

    
#     return ans



def solution(name):
    from collections import deque
    from copy import deepcopy
    alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic = {}
    start_string = 'A'*len(name)
    for idx, ab in enumerate(alphabet):
        dic[ab] = idx

    ud_cnt = 0
    for idx,lst in enumerate(zip(name,start_string)):
        i,j = lst[0],lst[1]
        
        tmp_cnt = min(abs(dic[i]-dic[j]) , abs(len(dic)-abs(dic[i]-dic[j])) )
        ud_cnt+= tmp_cnt # 위 아래로 커서를 누르는 횟수 
    
    def bfs(name):
        name_lst = list(name)    
        name_lst[0] = 'A'
        d = deque()
        d.append([name_lst,ud_cnt,0]) # lst,cnt,inx

        while d:
            
            arr,cnt,idx = d.popleft()
            
           
            arr[idx] = 'A'
     
            if arr.count('A') == len(name):
                return cnt
            
            for i in [-1,1]:
                
                new_arr = deepcopy(arr)
                
                d.append([new_arr,cnt+1,idx+i])
                
        
    return bfs(name)
            


print(solution('BB'))