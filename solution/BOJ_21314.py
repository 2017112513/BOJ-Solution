def biggest():
    answer = ''
    temp = 0
    flag = False
    for i in range(len(arr)):
        if arr[i] == 'M':
            if flag: # 앞에 수가 M이었음 
                temp*=10
            else:
                temp = 1
                flag = True
        else:
            if flag:
                temp = temp*10*5
                answer += str(temp)
                flag = False
            
            else:
                answer += '5'

    if arr[-1] == 'M':
        answer += '1'*len(str(temp))
    return answer 

def smallest():
    answer = ''
    temp = 0
    flag = False
    for i in range(len(arr)):
        if arr[i] == 'M':
            if flag: # 앞에 수가 M이었음 
                temp*=10
            else:
                temp = 1
                flag = True
        else:
            if flag:
                answer += str(temp)
                answer+='5'
                flag = False
            else:
                answer += '5'
    if arr[-1] == 'M':
        answer += str(temp)
    return answer 
import sys
input = sys.stdin.readline
n = input().rstrip()
arr = list(n)



b = biggest()
s = smallest()
print(b)
print(s)

