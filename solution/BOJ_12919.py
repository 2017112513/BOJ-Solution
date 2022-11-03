import sys
from collections import deque
input = sys.stdin.readline

S = input().strip()
T = input().strip()

d = deque()
d.append(T)

while d:
    x = d.popleft()

    if x == S:
        print(1)
        exit()

    if x[-1] == 'A':
        d.append(x[:-1])
        if T[0]=='B':
            d.append(x[::-1][:-1])
    else:
        if x[0] == 'B':
            d.append(x[::-1][:-1])
    
print(0)