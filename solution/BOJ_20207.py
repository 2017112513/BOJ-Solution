import sys
input = sys.stdin.readline
n = int(input())

arr = []
M = 0
for _ in range(n):
    s,e = map(int,input().split())
    arr.append([s,e])
    M = max(M,e)
arr =  sorted(arr,key=lambda x: (x[0],-(x[1]-x[0])))
visited = [0]*(M+2)

h = [0]*(M+2)

for s,e in arr:

    if s == e:
        h[s]+=1
        visited[s] +=1
        continue

    for i in range(s,e+1):
        if visited[i] == 0:
            visited[i] = 1

        h[i]+=1

answer = 0
max_h = 0
garo = 0
i = 1
while i<=M:

    if visited[i]==1:
        max_h = h[i]    
        garo = 1
        for j in range(i+1,M+2):
            if visited[j] == 0: # j전까지는 쭉 이어진 스케줄
                i = j
                answer += garo*max_h
                garo,max_h = 0,0
                break
            else:
                max_h = max(max_h,h[j])
                garo+=1
    i+=1

        
print(answer)

    