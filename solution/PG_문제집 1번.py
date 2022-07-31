from collections import defaultdict
def solution(x,y):
    answer = ''

    dic_x,dic_y = defaultdict(int),defaultdict(int)

    for i in x:
        dic_x[i] += 1
    for j in y:
        dic_y[j] += 1

    answer_list = []
    for i in range(10):
        i = str(i)
        if dic_x[i] and dic_y[i]:
            m = min(dic_x[i],dic_y[i])
            for j in range(m):
                answer_list.append(i)


    if answer_list:
        for i in sorted(answer_list,reverse=True):
            answer+=i
        if answer[0] == '0': # 이거때문에 ...
            answer = '0'
    else:
        answer = '-1'

    return answer 




# def solution(x,y):
#     answer = ''


#     visited_x ,visited_y = [0]*10,[0]*10

#     x_list,y_list = list(x),list(y)

#     for i in x_list:
#         visited_x[int(i)] += 1
#     for j in y_list:
#         visited_y[int(j)] += 1

#     answer_list = []
#     for i in range(10):
#         if visited_x[i]:
#             if visited_y[i]:
#                 m = min(visited_x[i],visited_y[i])

#                 for j in range(m):
#                     answer_list.append(i)


#     if answer_list:
#         for i in sorted(answer_list,reverse=True):
#             answer+=str(i)

#         if int(answer) == 0:
#             answer = '0'
#     else:
#         answer = '-1'

#     return answer 
# # 
# # 
