
def solution(num,cards):

    answer = float('inf')
    cards = [i for i in cards if i<num]


    flag = False
    
    for max_card in cards:
        
        temp = sorted([i for i in cards if i<=max_card],reverse=True)
        
        cnt = 0
        temp_num = num

        for card in temp:

            mok,nmg = temp_num//card , temp_num%card

            cnt+= mok

            temp_num = nmg
            
            if temp_num == 0:
                flag = True

                answer = min(answer,cnt)
                break

                
    
    if flag:
        return answer

    return -1
    



a = solution(num,cards)
print(a)
