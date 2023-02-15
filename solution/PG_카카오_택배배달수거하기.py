def solution(cap, n, deliveries, pickups):
    sorted_d = deliveries[::-1]
    sorted_p = pickups[::-1]

    
    deli = 0
    pick = 0
    
    
    answer  = 0
    
    for i in range(n):
        deli += sorted_d[i]
        pick += sorted_p[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2
    return answer