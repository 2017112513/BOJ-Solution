import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 끊어진 줄 개수, 브랜드 개수 

each,set = [] , []

for i in range(M):
    
    sp , p = map(int,input().split())
    
    set.append(sp)
    set.append(6*p)
    each.append(p)

set.sort()
each.sort()

answer = 0

mok,nmg = N//6 , N%6

answer = min((mok * set[0] + nmg * each[0]) , (mok+1) * set[0])

print(answer)

    