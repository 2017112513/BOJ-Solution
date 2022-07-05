from collections import deque
a,b = map(int,input().split())
cnt=0
d = deque()

lis_idx=[0]*100001
d.append(a)
while 1:
    x = d.popleft()
    if x==b:
        print(lis_idx[x])
        break
    lis = [x-1,x+1,2*x]
    for i in lis:
        if 0<=i<=100000 and not lis_idx[i]:
            lis_idx[i]=lis_idx[x]+1
            d.append(i)