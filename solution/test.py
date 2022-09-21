def solution(info,query):
    answer = []

    return answer



infos = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


from collections import defaultdict

total_dic = defaultdict(list)
# food_dic,age_dic,sort_dic = defaultdict(list),defaultdict(list),defaultdict(list)

for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        total_dic[lang + job + career + food].append(int(info[4]))


answer = []

for q in query:
    q = q.split()
    lang,job,career,food,score = q[0],q[2],q[4],q[6],q[7]
    lis = total_dic[lang+job+career+food]
    lis = sorted(lis)
    s,h = 0,len(lis)
    
    mid = 0
    while s<h:
        mid = (s+h)//2      
        if int(lis[mid]) >= int(score):
            h = mid 
        else:
            s = mid+1

    cnt = len(lis)-s

    print(cnt)





    
   


    

