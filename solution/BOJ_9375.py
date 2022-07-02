import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    dic = defaultdict(int)
    for j in range(n):
        _, sort = input().split()
        dic[sort] += 1
    answer = 1
    for key in dic:
        answer *= dic[key] + 1
    print(answer-1)