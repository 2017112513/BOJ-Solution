import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)],reverse = True)



answer = arr[0]
cnt = 1
for i in range(1,N):
    cnt += 1
    if answer > arr[i] * cnt:
        pass
    else:
        answer = arr[i] * cnt 
print(answer)

    
    

