
def search(x):
    global start

    visited[start][x] = 1
    for k in dic[x]:
        # print(x,k)
        if not visited[start][k]:
            visited[start][k] = 1
            search(k)
        else:
            continue
from collections import defaultdict , deque
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

dic = defaultdict(list)

visited = [[0]*N for _ in range(N)]


start = -1



one_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dic[i].append(j)
            one_list.append([i,j])




for i,j in one_list:

    start = i

    search(j)


for z in visited:
    print(*z)





                    



