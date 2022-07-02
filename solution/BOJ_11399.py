import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))

answer = 0
for i in range(n):
    answer += arr[i]*(n-i)

print(answer)