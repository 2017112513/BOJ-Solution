import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n,m,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.append([0]*m)
lis = list(range(m))
com = list(combinations(lis,3))

enemy = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            enemy.append([i,j])


answer = -1
for c in com:
    # print('='*20)
    # print(c)
    copy_arr = deepcopy(arr)
    acher = [[n,i]for i in c]
    cnt = 0

    while 1:
        flag = False
        enemy = [0]*3
        
        for i in range(n-1,-1,-1):
            for j in range(m):
                if copy_arr[i][j] == 1:
                    flag = True
                    for idx,X in enumerate(acher):
                        x,y = X[0],X[1]
                        if abs(x-i)+abs(y-j) <= d:
                    
                            if not enemy[idx]:
                                enemy[idx] = [abs(x-i)+abs(y-j),i,j]
                            else:
                                if enemy[idx][0] < abs(x-i)+abs(y-j):
                                    pass
                                elif enemy[idx][0] == abs(x-i)+abs(y-j):
                                    if enemy[idx][2]>y:
                                        enemy[idx] = [abs(x-i)+abs(y-j),i,j]  
                                else:
                                    enemy[idx] = [abs(x-i)+abs(y-j),i,j]  
        if flag == False:
            break
        

        for i in enemy:
            # print(i)
            if i:
                if copy_arr[i[1]][i[2]]:
                    copy_arr[i[1]][i[2]] = 0
                    cnt+=1 

            
        for i in range(n-1,-1,-1):
            for j in range(m):
                if copy_arr[i][j] == 1:
                    if i == n-1:
                        copy_arr[i][j] = 0
                    else:
                        copy_arr[i][j] = 0
                        copy_arr[i+1][j] = 1

        # for z in copy_arr:
        #     print(z)

    answer = max(cnt,answer)
        


print(answer)
                        
                            
                            


    






# 5 5 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 1 1 1