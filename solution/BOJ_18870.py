
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dic = {}
s = sorted(set(arr))

start = 0
for i in s:
    dic[i] = start
    start+=1

for i in arr:
    print(dic[i],end=' ')