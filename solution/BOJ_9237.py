import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())),reverse=True)
curr_day,last_day = 1,0

for i in arr:
    curr_day += 1
    
    last_day = max(last_day,curr_day + i)

print(last_day)

