

def roll_topni(num,roll_num):
    if roll_num == 1:
        arr[num].rotate(1)
    else:
        arr[num].rotate(-1)

def search_roll_num_dic():
    if not roll_flag:
        return dic
    dic = defaultdict(list)
    for i in range(4):
        flag = 0
        
        if i == 0:
            dic[i].append(0)
            flag_num =  arr[i][2]
            if flag_num != arr[i+1][6]:
                flag = 1
            flag_num = arr[i+1][2]
            dic[i].append(flag)
            dic[i+1].append(flag)

        elif i == 1:
            if flag_num != arr[i+1][6]:
                flag = 1
            flag_num = arr[i+1][2]
            dic[i].append(flag)
            dic[i+1].append(flag)
        

        elif i == 2:
            if flag_num != arr[i+1][6]:
                flag = 1
            flag_num = arr[i+1][2]
            dic[i].append(flag)
            dic[i+1].append(flag)
        
        else:
            dic[i].append(flag)
    
    return dic

def roll(num,roll_num,roll_flag):
    search_index = 0
    # print('num',num+1,roll_num)
    # print(dic)
    if roll_flag:
        roll_flag = False
        roll_topni(num,roll_num)
    else:
        new_roll_num = roll_num
    if roll_num==1:
        new_roll_num = -1
    else:
        new_roll_num = 1
    # print(arr)
    if num == 1 or num == 2:
        for p in [1,-1]:
            if p==1:
                search_index = 0
            else:
                search_index = -1    
            if dic[num+p][search_index]:
                if search_index == 0:
                    dic[num][-1] = 0
                else:
                    dic[num][0] = 0
                dic[num+p][search_index] = 0
                roll_topni(num+p,new_roll_num)
                roll(num+p,new_roll_num,roll_flag)

    elif num == 0:
        search_index = 0
        if dic[num+1][search_index]:
            dic[num][-1] = 0
            dic[num+1][search_index] = 0
            roll_topni(num+1,new_roll_num)
            roll(num+1,new_roll_num,roll_flag)

    else:       
        search_index = -1
        if dic[num-1][search_index]:
            dic[num][0] = 0
            search_index = 0
            dic[num-1][search_index] = 0
            roll_topni(num-1,new_roll_num)
            roll(num-1,new_roll_num,roll_flag)
            
    
import sys
from collections import deque,defaultdict
input = sys.stdin.readline


arr = []
diff = [0]*3
flag_num = -1
for i in range(4):
    lis = list(input().strip())
    d=deque(lis)
    arr.append(d)

# print()
for i in range(int(input())):
    roll_flag = True
    num,roll_num = map(int,input().split())



    dic = search_roll_num_dic()
    roll(num-1,roll_num,roll_flag)

    # for z in arr:
    #     print(z)



score_arr = [[0,1],[0,2],[0,4],[0,8]]
answer = 0
for i in range(4):
    answer += score_arr[i][int(arr[i][0])]



print(answer)
# 1 -> S
# 0 -> N
