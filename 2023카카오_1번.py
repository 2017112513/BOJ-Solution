today = "2022.05.19" 
terms = ["A 6","B 12","C 3"]
privacies= ["2021.05.02 A","2021.07.01 B","2022.02.19 C","2022.02.20 C"]
result =  []


from collections import defaultdict
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta


dic = defaultdict(list)
ty,tm,td = map(int,today.split('.'))
for idx,p in enumerate(privacies,1):
    date,cus  = p.replace('.','-').split()
    dic[cus].append([idx,date])
    

today = today.replace('.','-')

for t in terms:
    cus,curr_date = t.split()

    for idx,date in dic[cus]:
        month_before = (datetime.strptime(date, '%Y-%m-%d') + relativedelta(months = int(curr_date))).strftime('%Y-%m-%d')
        curr_day = datetime(ty,tm,td)
        y,m,d = map(int,month_before.split('-'))
        in_day = datetime(y,m,d)

        if not curr_day<in_day:
            result.append(idx)


    

        