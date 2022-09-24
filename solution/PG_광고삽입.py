# 반례가 있담녀 100시간을 넘길경우? 

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]


def after_adv(st):

    adv_H,adv_M,adv_S = map(int,adv_time.split(':'))
    H,M,S = st[0],st[1],st[2]

    H += adv_H
    M += adv_M
    S += adv_S

    if S>60:
        minute = S//60
        second = S%60
        M+=minute
        S = second
      
    if M>60:
        hour = M//60
        minute = M%60
        H+=hour
        M = minute

    return H,M,S


start_time = []
start_time.append(list(map(int,"00:00:00".split(':'))))
end_time = []


for log in logs:
    st,et = log.split('-')
    start_time.append(list(map(int,st.split(':'))))
    end_time.append(list(map(int,et.split(':'))))
end_time.append(list(map(int,play_time.split(':'))))

bin = []

for st in start_time:
    bin.append(st)

for et in end_time:
    bin.append(et)

bin = sorted(bin,key=lambda x: (x[0],x[1],x[2])) # 각 인덱스 별로 시청자 수를 구분하기 위해 정의 






for st in start_time:
    before_H,before_M,before_S = map(int,adv_time.split(':')) # 광고 시작 시간 
    after_H,after_M,after_S = after_adv(st) #광고 시작 후 끝나는 시간 

    for log in logs:
        st,et = log.split('-') # 
        start_H,start_M,start_S = map(int,st.split(':')) # 시청 시작 시간
        end_H,end_M,end_S = map(int,st.split(':')) # 시청 끝 시간
        
        if start_H<=after_H and start_M<=after_M and after_S<=after_S:
            if end_H>=before_H and end_M>=before_M and end_S>=before_S:
                for bt in bin:
                    while start_H<=bt[0] and start_M<=bt[1] and start_S<=bt[2]:

    



    