

def solution(beginning,target):
    def reverse_num(x):
        if x == 0:
            return 1
        return 0

    def reverse_row(i,copy_arr):
        for j in range(len(copy_arr[i])):
            copy_arr[i][j] = reverse_num(copy_arr[i][j])
        return copy_arr

    def reverse_col(i,copy_arr):
        for r in range(len_row):
            copy_arr[r][i] = reverse_num(copy_arr[r][i])
        return copy_arr


    from collections import deque
    from copy import deepcopy

    d = deque()
    visited = []

    d.append([0,beginning])
    answer = -1


    len_row = len(beginning)
    len_col = len(beginning[0])

    while d:
        cnt,lis = d.popleft()
        # print(cnt,lis)
        if target == lis:
            answer = cnt
            break

        for i in range(len_row):
            copy_lis = deepcopy(lis)
            copy_lis = reverse_row(i,copy_lis)

            if copy_lis not in visited:
                visited.append(copy_lis)
                d.append([cnt+1,copy_lis])

        for i in range(len_col):
            copy_lis = deepcopy(lis)
            copy_lis = reverse_col(i,copy_lis)
            if copy_lis not in visited:
                visited.append(copy_lis)
                
                d.append([cnt+1,copy_lis])

    return answer


