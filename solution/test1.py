from collections import deque ,defaultdict

prices = [1,2,3,2,3]

def solution(prices):
    answer = [] 
    
    #인덱스를 Key로 담는 True/False 딕셔너리 
    idx_price = {key: True for key, value in enumerate(prices)}
    #가격을 Key , 인덱스 리스트를 Value로 하는 딕셔너리 하나 
    price_dic = defaultdict(list)

    for idx, i in enumerate(prices):
        price_dic[i].append(idx)

    print(idx_price)
    print(price_dic)
     
    
    
    return answer 

a = solution(prices)

print(a)