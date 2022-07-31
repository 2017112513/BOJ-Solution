def reverse_num(x):
    if x == 0:
        return 1
    return 0
# arr = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
# target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

arr = [[0,0],[0,0]]
target = [[0,0],[1,1]]


from collections import deque

d = deque()

visited = []

d.append([0,arr,[]])
answer = -1

len_row = len(arr)
len_col = len(arr[0])

while d:
    print(d)
    cnt,lis,reverse_list = d.popleft()

    # for x,y in reverse_list:
    #     lis[x][y] = reverse_num(lis[x][y])
    

    if lis not in visited:
        visited.append(lis)
    else:
        continue
    
    if target == lis:
        answer = cnt
        break

    for i in range(len_row):
        next_reverse_list = []
        for j in range(len_col):
            next_reverse_list.append([i,j])
    
        d.append([cnt+1,lis,next_reverse_list])

    # for i in range(len_col):
    #     next_reverse_list = []
    #     for j in range(len_row):
    #         next_reverse_list.append([j,i])

    #     d.append([cnt+1,lis,next_reverse_list])
    

