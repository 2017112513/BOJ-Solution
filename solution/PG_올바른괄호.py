from collections import deque 

def solution(s):

    s_list = deque(s)
    
    left = deque()
    right = deque()
    
    while s_list:
        
        x = s_list.popleft()
        
        if x == '(':
            left.append(x)
        else:
            
            if not left:
                return False
            left.popleft()
        
    if left:
        return False
            
            
        
        

    return True