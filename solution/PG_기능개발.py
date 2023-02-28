from collections import deque 
def solution(progresses, speeds):
    answer = []
    
    
    
    dp = deque(progresses)
    ds = deque(speeds)
    temp = deque()
    
    while dp:
    
        job = dp.popleft()
        speed = ds.popleft()
        
        day = 0
        while job<100:
            job += speed
            
            day += 1
            
        temp.append(day)
    
    start = temp.popleft()
    
    if not temp:
        return [1]
    cnt = 1
    while temp:
        next_start = temp.popleft()
        
        if next_start<=start:
            cnt += 1
        else:
            answer.append(cnt)
            start = next_start
            cnt = 1
            
    answer.append(cnt)
    return answer
        
            
