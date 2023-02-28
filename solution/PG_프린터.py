from collections import deque ,Counter

def solution(priorities, location):
    answer = 0

    
    M = max(priorities)
    
    while priorities:

        x = priorities.pop(0)
            
        if x == M:
            if location == 0: # 내가 원하는 수 
                return answer + 1
            
            answer += 1 
        
            M = max(priorities)
                    
            location -= 1
        else: # 밖으로 나온 값이 최대값이 아니라면 
            if location == 0 :
                location = len(priorities)
            else:
                location -= 1
            priorities.append(x)
                
            
        
        
                    

    return answer