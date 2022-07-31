
import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())))

answer = 0
while arr:
    if not answer:
        answer += arr.pop()
    else:
        answer += arr.pop()/2


print(answer)