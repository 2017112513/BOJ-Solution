n = 5
cost = [10,20,14,40,50]
x = 70


def solution(n,cost,x):
    
    answer = 0

    from collections import deque
    LIMIT = 10**9 + 7
    d = deque()

    d.append((x,0,0)) #남은 금액 , 물감 개수  , 현재 물감 위치
    d.append((x,0,0)) 
    
    while d:
        
        curr_cost,curr_cnt,curr_idx = d.popleft()
        print(curr_idx) 
        if curr_idx == n: 

            answer = max(answer,curr_cnt) 
            continue

        if curr_cost>=cost[curr_idx]:
            
            next_cnt = curr_cnt + 2**curr_idx
            next_cost = curr_cost - cost[curr_idx]
        

            if next_cnt>= LIMIT:
                next_cnt = next_cnt % LIMIT


            d.append([next_cost,next_cnt,curr_idx+1]) # 현재 위치에 있는 물건을 살 경우

            d.append([curr_cost,curr_cnt,curr_idx+1]) # 현재 위치에 있는 물건을 사지 않을 경우

        else:

            d.append([curr_cost,curr_cnt,curr_idx+1]) # 현재 위치에 있는 물건을 사지 못하는 경우

    return answer


a = solution(n,cost,x)
print(a)