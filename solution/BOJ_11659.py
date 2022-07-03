import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = list(map(int,input().split()))
ans_list = [0]
summary = 0

for i in arr:
    summary+=i
    ans_list.append(summary)

for _ in range(m):
    start,end = map(int,input().split())
    print(ans_list[end]-ans_list[start-1])