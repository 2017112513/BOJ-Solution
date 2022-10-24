import sys
input= sys.stdin.readline
L,C = map(int,input().strip().split())

def backtracking(moem,jaem,password):
    # print(password)
    if len(password) == L:
        if moem>0 and jaem>1:
            return answer.append(''.join(sorted(password)))
    else:
        vis = ''.join(sorted(password))
        if not visited[vis]:
            visited[vis] = 1
            for s in string:
                if s in ['a','e','i','o','u']:
                    if s not in password:
                        # print(password,s)
                        backtracking(moem+1,jaem,password+s)
                else:
                    if s not in password:
                        # print(password,s)
                        backtracking(moem,jaem+1,password+s)
        

string = list(input().split())
from collections import defaultdict
visited=defaultdict(int)
answer = []
for s in string:

    moem,jaem = 0,0
    if s in ['a','e','i','o','u']:
        moem+=1
    else:
        jaem+=1

    ans = backtracking(moem,jaem,s)
    

for i in sorted(set(answer)):
    print(''.join(i))