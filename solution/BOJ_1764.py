from collections import defaultdict
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())

answer = []

dic = defaultdict(int)

for i in range(n+m):
    key = input().strip()
    dic[key] += 1
    if dic[key] == 2: # 듣보잡이라는 뜻
        answer.append(key)
answer = sorted(answer)
print(len(answer))
print('\n'.join(answer))