from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
answer = []
for _ in range(T):
    
    flag = True # True 면 popleft() , False 면 pop()

    command = deque(input().strip().replace('RR',''))
    n_ = input()
    
    d = deque(input().strip()[1:-1].split(','))


    E = False
    while command:
        
        com = command.popleft()
    
        if com =='R':
            if flag:
                flag = False
            else:
                flag = True

        else:
            if not d:
                E = True
                break
            if flag:
                x = d.popleft()      
            else:
                x = d.pop()
        

    if E:
        answer.append('error')
    else:
        if flag:
            answer.append(list(map(int,d)))
        else:
            answer.append(list(map(int,d))[::-1])
    
for i in answer:
    if type(i)== list:
        print('[',end='')
        for j in range(len(i)):
            if j == len(i)-1:
                print(i[j],end='')
            else:
                print(i[j],end=',')
        
        print(']')
    else:
        print(i)
    
    

