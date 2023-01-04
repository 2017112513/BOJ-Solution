import sys
from collections import deque
from heapq import heappop,heappush
def bfs():
    answer_list = [10**9]*N
    h = []
    heappush(h,(0,0)) # cnt , 출발 지점
    
    while h:
        cnt, x = heappop(h)
        if x == N-1:
            return cnt   
        if arr[x] == 0:
            continue

        for i in range(arr[x]+1):
            if x+i<N and answer_list[x+i]>cnt+1:
                answer_list[x+i] = cnt+1
                heappush(h,(cnt+1,x+i))
    return -1

if __name__ == '__main__':
    
    N = int(input())
    arr = list(map(int,input().split()))

    answer = bfs()

    print(answer)
    
