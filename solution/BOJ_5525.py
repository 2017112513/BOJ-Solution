import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

string = 'I' + 'OI'*n

S = input().strip('O').replace('IO','R')

start = 0
cnt = 0 
answer = 0
while 1:
  
    if S[start]== 'R':
        cnt+=1
    else:
        cnt = 0

    if cnt==n and start<len(S):
        
        if S[start+1] == 'I':
    
            answer += 1
            cnt = 0
        elif S[start+1] == 'R':
    
            answer += 1
            cnt-=1 
        else:
            cnt=0
    
    start+=1
    if start == len(S)-1:
        break
    

print(answer)