from collections import defaultdict
def solution(id_list,report,k):
    
    dic_singo_cnt = defaultdict(int) #value 유저가 신고당한 횟수
    dic_singo_list = defaultdict(list) #value 신고한사람들 : key
    for i in set(report):
        key,value = i.split()
        dic_singo_list[value].append(key)
        dic_singo_cnt[value] += 1
    
    answer_dic = defaultdict(int)
    
    for key in dic_singo_cnt.keys():
        if dic_singo_cnt[key]>=k:
            for v in dic_singo_list[key]:
                answer_dic[v]+=1

    answer=[]

    for name in id_list:
        answer.append(answer_dic[name])
    
    return answer