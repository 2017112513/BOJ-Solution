from collections import deque

def solution(order):
    origin = deque(sorted(order))
    sub = deque()

    ans = 0
    for od in order:
        flag = True

        if sub and sub[0] == od:
            sub.popleft()
            ans+=1
            continue

        if od>=origin[0]:
            while 1:
                x = origin.popleft()
                if x == od : 
                    ans+=1
                    flag = False
                    break
                else:
                    sub.appendleft(x)
        if not flag:
            continue

        if (sub and sub[0] != od) and origin[0]!=od:
            break

        return ans

                
        
