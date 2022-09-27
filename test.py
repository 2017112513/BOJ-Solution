T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr = sorted(arr,key=lambda x: (x[0],x[1]))
    
    rank = [0]*(N+1)

    r = 0
    cnt= 0
    for i in range(N):
        if r == 0 : 
            r = arr[i][1] 
            rank[i] = r 
        else:
            if r>arr[i][1]:
                r = arr[i][1] 
                rank[i] = r
            else:
                rank[i] = r
    # print(arr)    
    # print(rank)
    for i in range(N-1,-1,-1):
        if arr[i][1]>rank[i]:
            cnt+=1

    print(N-cnt)

    

        
        
