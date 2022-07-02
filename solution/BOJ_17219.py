import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())

dic  = {}
for _ in range(n):
    
    domain,password = input().strip().split()
    dic[domain] = password

for _ in range(m):
    print(dic[input().strip()])