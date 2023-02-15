def is_inner(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

def spring(feed,arr,dead):
    fall_list = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                temp = deque()
                arr[i][j] = deque(sorted(arr[i][j]))
                while arr[i][j]:
                    namu = arr[i][j].popleft()
                    if feed[i][j]>=namu:
                        feed[i][j] -= namu
                        temp.append(namu+1)
                        if (namu+1) % 5 == 0:
                            fall_list.append((i,j,namu+1))
                    else:
                        dead[i][j]+=namu // 2
                arr[i][j] = temp
    
    return feed,arr,dead,fall_list

def summer(dead):
    for i in range(N):
        for j in range(N):
            if dead[i][j]:
                feed[i][j] += dead[i][j]
                dead[i][j] = 0

    return dead

def fall(fall_list,arr):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    while fall_list:
        x,y,namu = fall_list.popleft()
        
        for i in range(8):
            a,b, = x+dx[i],y+dy[i]
            if is_inner(a,b):
                arr[a][b].append(1)
    
    return arr

def winter(feed):
    for i in range(N):
        for j in range(N):
            feed[i][j] += A[i][j]
    return feed


import sys
from collections import deque 

if __name__ == '__main__':

    input  = sys.stdin.readline

    N,M,K = map(int,input().split())

    A = [list(map(int,input().split())) for _ in range(N)]

    feed = [[5]*N for _ in range(N)]
    arr = [[deque() for _ in range(N)] for _ in range(N)]
    dead = [[0]*N for _ in range(N)]

    for _ in range(M):
        r,c,age = map(int,input().split())
        arr[r-1][c-1].append(age)
    
    for _ in range(K):

        feed,arr,dead,fall_list = spring(feed,arr,dead)
        dead = summer(dead)
        arr = fall(fall_list,arr)
        feed = winter(feed)
        



    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(arr[i][j])
    
    print(answer)
        

