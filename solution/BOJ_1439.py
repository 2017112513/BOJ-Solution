import sys
from collections import Counter
input = sys.stdin.readline

S = list(input().strip())

lis = []

while S:
    x = S.pop()

    if not lis: 
        lis.append(x)
    else:
        if lis[-1] != x:
            lis.append(x)

print(min(Counter(lis).values()) if len(lis)>1 else 0)


    