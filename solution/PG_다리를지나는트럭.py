from collections import deque

def solution(bl, weight, truck_weights):
    
    bridge = deque([0 for _ in range(bl)])
    time = 0 
    
    truck_weights = deque(truck_weights)
    curr_weight = 0 
    while bridge:
        
        x = bridge.popleft()
        curr_weight -= x
        time += 1
        
        if not truck_weights:
            continue
            
        if curr_weight + truck_weights[0] <= weight:
            
            x = truck_weights.popleft()
            bridge.append(x)
            curr_weight += x
        else:
            
            bridge.append(0)
            

    return time 
                

