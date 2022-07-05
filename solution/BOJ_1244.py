

from re import A
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque((list(map(int,input().split()))))
arr.appendleft(0)

def change_switch(x):
    if x:
        return 0
    else:
        return 1

T = int(input())
for _ in range(T):
    s,n = map(int,input().split())

    if s == 1:
        for i in range(n,N+1,n):
         
            arr[i] = change_switch(arr[i])
    else:
        if n==1 and n==N:
            arr[n] = change_switch(arr[n])
        else:
        
            arr[n] = change_switch(arr[n])
            start = 1
            flag = True
            change_list = []
            while flag:
                if 1<=n+start<=N and 1<=n-start<=N:
                    if arr[n+start] == arr[n-start]:
                
                        change_list.append(n+start)
                        change_list.append(n-start)
                        start+=1
                    else:
                        flag = False
                else:
                    break
            # print(n,change_list)
            for j in change_list:
                arr[j] = change_switch(arr[j])


arr = list(arr)[1:]

for i in range(len(arr)):
    if i%20 == 0 and i!=0:
        print()
    print(arr[i],end=' ')
    