def trac(x,answer_str):
    if len(answer_str)==M:
        for s in str(answer_str):
            print(s,end = ' ')
        print()
    else:
        for i in arr:
            if x != i and str(i) not in answer_str:
                trac(i,answer_str+str(i))
    

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
answer = []
arr = [i for i in range(1,N+1)]
visited =  [0]*(N+1)

for i in arr:
    answer_str = ''
    if not visited[i]:
        visited[i] = 1
        answer_str += str(i)
        trac(i,answer_str)
