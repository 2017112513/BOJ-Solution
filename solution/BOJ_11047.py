import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())

arr = []

for _ in range(n):
    value = int(input())
    if value <= m: # m보다 큰 금액이면 필요 없음
        arr.append(value)

arr = sorted(arr,reverse=True)

answer = 0

for i in arr:

    if m == 0:
        break
    if i>m:
        continue
    
    answer += m//i
    m = m%i

print(answer)