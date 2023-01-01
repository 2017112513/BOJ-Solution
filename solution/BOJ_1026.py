import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())),reverse=True)

answer = 0
for a,b in zip(A,B):
    answer += a*b

print(answer)

