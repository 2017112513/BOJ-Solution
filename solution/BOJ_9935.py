import sys
input = sys.stdin.readline
from collections import deque


S = input().strip()
k = list(input().strip())

len_k = len(k)
d =deque(S)

stack=[]


while d:
    
    x = d.popleft()
    stack.append(x)
    
    if len(stack)>=len_k and stack[-1] == k[-1]:
        if stack[-len_k:] == k:
            for _ in range(len_k):
                stack.pop()


print(''.join(stack) if stack else 'FRULA')
            

        