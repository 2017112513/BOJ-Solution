import sys
input = sys.stdin.readline
from collections import defaultdict
T = int(input())

for _ in range(T):
    flag = False    
    n = int(input())
    arr = list((input().strip() for _ in range(n)))
    
    dic = defaultdict(int)
    for number in arr:
        S = ''
        for num in number:
            S+=num
            dic[S]+=1
  
    for number in arr:
        if dic[number]>1:
            flag = True

    print('NO' if flag else 'YES')
    
        

    
    

    

