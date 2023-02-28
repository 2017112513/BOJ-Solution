from collections import defaultdict
from collections import deque 
def bfs(N,begin,target,arr):
    
    
    d = deque()
    visited = [0]*N
    visited[begin] = 1
    d.append((0,begin,visited))
    
    for z in arr:
        print(z)
    answer = 10**9
    
    while d:
        cnt,word_number,temp_visited = d.popleft()
        if word_number == target:

            answer = min(answer,cnt)

        for i in range(N):
            if arr[word_number][i] == 1 and temp_visited[i] == 0:
                temp_visited[i] = 1
                d.append((cnt+1,i,temp_visited))
                
    if answer == 10**9:
        return 0 
    return answer
            
def solution(begin, target, words):

    if target not in words:
        return 0
    
    N = len(words)
    arr = [[0]*N for _ in range(N)]
    
    words_dict = defaultdict(int)
    for i in range(len(words)):
        words_dict[i] = words[i]
        if words[i] == begin: 
            b_number = i 

        if words[i] == target: 
            t_number = i 

        for j in range(len(words)):
            if i == j : 
                continue
            p , q = words[i] , words[j]
            cnt = 0
            for left, right in zip(p,q):

                if left != right:
                    cnt += 1

            arr[i][j] = cnt 
            arr[j][i] = cnt

    #=============================

    answer = bfs(N,b_number,t_number,arr)
    return answer

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
words.append(begin)
a = solution(begin,target,words)

print(a)