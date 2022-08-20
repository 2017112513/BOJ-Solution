
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
        print(c)
        break
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


# solution(["banana", "apple", "rice", "pork", "pot"]	,[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	)