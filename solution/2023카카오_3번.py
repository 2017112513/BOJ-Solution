# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]


# emoticons = [1300, 1500, 1600, 4900]

users = [[40,10000],[25,10000]]
emoticons = [7000,9000]
#def solution''''''''''''''''''''''''''''''''

dc = [10,20,30,40]
from itertools import product
dc_list = list(product(dc,repeat = len(emoticons)))


answer_list = []
for percent_list in dc_list:
    new_emoticons = [[i,j] for i,j in zip(percent_list,emoticons)]
    cnt = 0 
    total_price = 0

    for user_per,user_price in users:
        user_com = 0 # 유저가 소비한 돈 

        for percent,emo in new_emoticons:
            if percent>=user_per:

                emo = emo*(100-percent)*0.01
                user_com+= emo

        if user_com>user_price:
            cnt+=1
        else:
            total_price+=user_com
       
    answer_list.append([cnt,int(total_price)])
 

answer_list = sorted(answer_list,key=lambda x: (-x[0],-x[1]))
answer = answer_list[0]

print(answer)

