def solution(string):
    
    reverse_string = string[::-1]
    
    if string == reverse_string:
        return 0


    flag = 0 
    start,end = 0,len(string)-1
  
    while end>=start:
     
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:

            flag = 0 
            temp = string[start+1:end+1]
        
            if temp == temp[::-1] : 
                flag +=1 
            temp = string[start:end]
    
            if temp == temp[::-1] : 
                flag +=1 

            if flag> 0:
                return 1
            return 2


    

        
        
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    
    string = input().strip()
    answer = solution(string)
    print(answer)
