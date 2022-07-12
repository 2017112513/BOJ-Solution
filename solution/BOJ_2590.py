def solution(n):
    if n == 6:
        return arr[6]

    elif n==5:
        
        if arr[5] == 0:
            return 0

        cnt = arr[5]
        arr[5] = 0
        if arr[1]>11*cnt:
            arr[1]-=11*cnt
        else:
            arr[1] = 0
        return cnt

    elif n==4:
        if arr[4] == 0:
            return 0
        cnt = arr[4]
        arr[4] = 0
        if arr[2]>5*cnt:
            arr[2]-=5*cnt
        else:
            sec = arr[2]
            arr[2] = 0
            if 20*cnt- 4*sec>0:
                dummy = 20*cnt-4*sec
                if arr[1]:
                    if dummy>arr[1]:
                        arr[1] = 0
                    else:
                        arr[1] -= dummy
        return cnt

    elif n==3:
        if arr[3] == 0:
            return 0
        if (arr[3]%4) == 0:
            cnt = (arr[3]*9)//36
            arr[3] = 0
        else:
            cnt = (arr[3]*9)//36 + 1
            arr[3] = arr[3]%4
           
            if arr[3]==3:
                if arr[2]:
                    arr[2]-= 1
                    if arr[1]>5:
                        arr[1] -= 5
                    else:
                        arr[1] = 0
                else:
                    if arr[1]>9:
                        arr[1] -= 9
                    else:
                        arr[1] = 0
            elif arr[3] == 2:
                if arr[2]>3:
                    arr[2] -= 3
                else:
                    sec = arr[2]
                    arr[2]=0
                    dummy = 18-sec*4
                    if arr[1]>dummy:
                        arr[1] -= dummy 
                    else:
                        arr[1] = 0
            elif arr[3] == 1:
                if arr[2]>5:
                    arr[2] -= 5
                else:
                    sec = arr[2]
                    arr[2]=0
                    dummy = 27-sec*4
                    if arr[1]>dummy:
                        arr[1] -= dummy 
                    else:
                        arr[1] = 0

            arr[3] = 0
        return cnt
                
    elif n==2:
        if arr[2] == 0:
            return 0 
        if (arr[2]%9) == 0:
            cnt = (arr[2]*4)//36
            arr[2] = 0
        else:
            cnt = (arr[2]*4)//36 + 1
            arr[2] = arr[2]%9
            if arr[1]>36-4*arr[2]:
                arr[1]-= (36-4*arr[2])   
            else:
                arr[1] = 0
        return cnt

    else:
        if (arr[1]%36) == 0:
            cnt = (arr[1]*1)//36
            arr[1] = 0
        else:
            cnt = (arr[1]*1)//36 + 1

        return cnt



import sys
input =  sys.stdin.readline

answer = 0

arr = [0]
for _ in range(6):
    arr.append(int(input().rstrip()))

for i in range(6,0,-1):
    s = solution(i)
    print(i,arr)
    answer+=s

print(answer)