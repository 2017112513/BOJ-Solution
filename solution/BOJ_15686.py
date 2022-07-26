def bfs():
    answer = float('inf')
    while chicken_list:
        chicken_jip = chicken_list.pop()
        city_distance = 0

        for h in home:
            chicken_distance = float('inf')
            home_x,home_y = h[0],h[1]
            # print(home_x,home_y)
            for cj in chicken_jip:
                chicken_x,chicken_y = cj[0],cj[1]
                distance = abs(home_x-chicken_x) + abs(home_y-chicken_y)
                chicken_distance = min(chicken_distance,distance)
            # print(chicken_distance)
            city_distance += chicken_distance
        answer = min(answer,city_distance)
        # print(answer)

    return answer

from itertools import combinations

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)] # 1-집 2-치킨집

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j]) 

chicken_list = list(combinations(chicken,M))
print(chicken_list)
m = bfs()

print(m)


