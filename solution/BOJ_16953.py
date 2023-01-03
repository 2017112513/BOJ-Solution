import sys
from collections import deque,defaultdict
input= sys.stdin.readline



A,B = map(int,input().split())
dic = defaultdict(int)
d = deque()
d.append((0,A))

flag = False

while d:
    cnt,x = d.popleft()

    if x==B:
        flag = True
        print(cnt+1)
    elif x>B:
        continue

    temp = str(x)+'1'
    if not dic[temp]:
        dic[temp] = 1
        d.append((cnt+1,int(temp)))
    
    temp = x*2
    if not dic[temp]:
        dic[temp] = 1
        d.append((cnt+1,temp))

if not flag:
    print(-1)
        