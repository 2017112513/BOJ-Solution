import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

arr = sorted(arr,key=lambda x : (x[1],x[0]))
print(arr)
answer = 0
last = 0
for i,j in arr:
    if i>=last:
        last = j
        answer+=1
print(answer)
