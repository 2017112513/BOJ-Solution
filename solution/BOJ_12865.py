import sys
input = sys.stdin.readline

N,K = map(int,input().split())

weight , value = [0] , [0]

for _ in range(N):
    
    W,V = map(int,input().split())

    weight.append(W)
    value.append(V) 


arr = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        w = weight[i]
        v = value[i]
        if j<w:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j],arr[i-1][j-w]+v)
for z in arr:
    print(z)

print(arr[-1][-1])


    
'''
10 15
1 1
2 3
5 3
5 1
4 5
3 3
3 2
4 4
4 4
4 3
'''


