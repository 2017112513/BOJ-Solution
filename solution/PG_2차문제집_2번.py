from collections import Counter
def solution(topping):
    
    answer = 0

    if len(topping)==1:
        return 0

    first = topping[0:1]
    second = topping[1:]

    first_c = Counter(first)
    second_c = Counter(second)

    cnt_f = len([key for key,value in first_c.items() if value>0])
    cnt_s = len([key for key,value in second_c.items() if value>0])

    if cnt_f == cnt_s:
        return 1
    
    for i in range(1,len(topping)): 
        flavor = topping[i]

        second_c[flavor] -= 1
        if second_c[flavor] == 0:
            cnt_s -= 1
     

        if flavor in first_c:
            first_c[flavor] += 1
        else:
            first_c[flavor] = 1
            cnt_f += 1
        
        if cnt_s == cnt_f:
            # print(first_c,second_c)
            # print(i)
            answer +=1




    
    return answer



