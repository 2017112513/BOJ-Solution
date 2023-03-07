from heapq import heappush,heappop
def solution(operations):
    
    answer = []
    min_h , max_h = [], []
    
    for command in operations:
        print(command,min_h,max_h)
        c , num = command.split()
        
        if c == 'I':
            heappush(min_h,int(num))
            heappush(max_h,-1*int(num))
        else:
            if num == "1" and max_h: # 최대값 pop 
                M = heappop(max_h) # M은 최대값 
                flag = True 
                
                cnt = len(min_h)
                new_min_h = []
                for _ in range(cnt):
                    
                    x = -1*heappop(min_h)
                    
                    if x == M and flag:
                        flag = False
                        continue
                        
                    heappush(new_min_h,-1*x)
                min_h = new_min_h
                    
            elif num == "-1" and min_h: # 최소값 pop
                M = heappop(min_h) # M은 최소값 

                flag = True 
                cnt = len(max_h)
                new_max_h = []
                for _ in range(cnt):
                    
                    x = -1*heappop(max_h)

                    if x == M and flag:
                        flag = False
                        continue
                        
                    heappush(new_max_h,-1*x)
                max_h = new_max_h
    if min_h:
        answer = [max(min_h),min(min_h)]
    else:
        answer = [0,0]
    return answer
