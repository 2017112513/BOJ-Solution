import sys
input = sys.stdin.readline


arr = sorted((list(input().strip())),reverse=True)

if '0' in arr:

    total = 0 
    for i in arr:
        total += int(i)

    if total % 3 == 0:
        print(''.join(arr))
    else:
        print(-1)
else:
    print(-1)




