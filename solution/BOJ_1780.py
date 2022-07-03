import sys
input = sys.stdin.readline
answer = [0]*3
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

def solution(N,array):
    flag = True
    x,y = 0,0
    start = array[0][0]
    for i in range(N):
        for j in range(N):
            if i==0 and j==0:
                continue
            if start != array[i][j]:
                flag=False
                cnt = 0
                new_N = N//3
                
                while y<N:
                    
                    cnt+=1
                    new_array=[]
                    for p in range(x,x+new_N):
                        new_array.append(array[p][y:y+new_N])
     
                    if new_array:
                        solution(new_N,new_array)
        
                    x+=new_N
                    if x == N:
                        x = 0

                    if cnt%3==0:
                        y+=new_N
    
                for_flag = False
                break


    if flag:
        answer[array[0][0]]+=1
solution(N,arr)
print(answer[-1])
print(answer[0])
print(answer[1])

