def rank(cnt):
        if cnt <= 1:
            return 6
        elif cnt == 2:
            return 5
        elif cnt == 3:
            return 4
        elif cnt == 4:
            return 3
        elif cnt == 5:
            return 2
        else:
            return 1

def solution(lottos,win_nums):




    cnt = 0
    zero_cnt = 0
    win_num_list = [0]*(45+1)
    
    for i in win_nums:
        win_num_list[i] = 1

    for i in lottos:
        if i == 0:
            zero_cnt+=1
        if win_num_list[i]:
            cnt+=1
    print(cnt,zero_cnt)
    answer = [rank(cnt+zero_cnt),rank(cnt)]

    return answer

    
    

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

ans = solution(lottos,win_nums)
print(ans)

