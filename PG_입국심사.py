n = 6 
times = [7,10]
# def solution(n,times):
#     from heapq import heappush,heappop

#     h = [] 

#     for time in times:
#         heappush(h,[time,0])
#     cnt = 0
#     while 1: 
#         if cnt==n:
#             break
#         end_time,start_time = heappop(h)
#         add_time = end_time - start_time
        
#         heappush(h,[end_time+add_time,end_time])
#         cnt+=1 

#     return end_time

# solution(n,times)

def solution(n,times):
    times = sorted(times)
    M = max(times)*n
    m = 0
    answer = 0

    while m<=M:
        mid = (M+m)//2
        numbers = 0

        for time in times:
            numbers += (mid//time)

            if numbers>=n:
                M = mid-1
                answer = mid 
                break
        if numbers<n:
            m = mid+1
    
    return answer

    

a = solution(n,times)

            

