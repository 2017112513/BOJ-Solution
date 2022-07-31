
from collections import Counter    
def solution(want,number,discount):
    
    answer = 0
    dic = {}

    for i in range(len(want)):
        dic[want[i]] = number[i]
    length = len(discount)

    for i in range(0,length-9):
        flag = True
        c = Counter(discount[i:i+10])
        for key,value in dic.items():
            if key not in c:
                flag = False
                break
            
            if key in c and c[key]<value:
                flag = False
                break

        if flag:
            # print(i)
            answer+=1

    return answer