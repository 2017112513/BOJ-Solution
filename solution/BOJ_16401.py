import sys
input = sys.stdin.readline

N , M = map(int,input().split())

arr = list(map(int,input().split()))

left , right = 0 , max(arr)
answer = 0
flag = True
while left<=right:

    mid = (left + right) // 2 
    if mid == 0:
        print(0)
        flag = False
        break
    temp = [ i//mid for i in arr if i>=mid]
    
 
    if sum(temp) >= N:
        left = mid+1 
        answer = max(mid,answer)
    else:
        right = mid-1
    
print(answer if flag)