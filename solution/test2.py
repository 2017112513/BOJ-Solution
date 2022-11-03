v1 = [0,0,1,2,2,]
v2 = [1,2,3,3,4]
a = 0
b = 3

def solution(v1,v2,a,b):
    
    from collections import defaultdict

    answer = -1

    
    dic =  defaultdict(list)

    a_list = [0]

    for i,j in zip(v1,v2): 
        dic[i].append(j)
        dic[j].append(i)

    friend = dic[b]

    for i in friend:


    return answer