
import sys
input = sys.stdin.readline
n = input()
lis = n.split('-')
answer = 0
flag = True

for i in range(len(lis)):
    print(i,lis[i])
    if i==0 and lis[i]=='':
        flag = False #다음수는 음수처리
        continue
    elif i==0 and lis[i]!='':
        answer+=sum(map(int,lis[i].split('+')))
        continue

    if i==1 and not flag:
        answer -= sum(map(int,lis[i].split('+')))
        continue
    
    
    answer -= sum(map(int,lis[i].split('+')))
    
print(answer)

