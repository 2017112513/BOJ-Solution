import sys
input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    do= input().split()
    if do[0]=='add':
        if int(do[1]) in s:
            continue
        s.add(int(do[1]))
    elif do[0] == 'remove':
        if int(do[1]) not in s:
            continue
        s.remove(int(do[1]))
    elif do[0] == 'check':
        if int(do[1]) in s:
            print(1)
        else:
            print(0)
    elif do[0] == 'toggle':
        if int(do[1]) in s:
            s.remove(int(do[1]))
        else:
            s.add(int(do[1]))
    elif do[0] == 'all':
        s = set(range(1,20+1))
    elif do[0] == 'empty':
        s = set()