
from collections import deque
def next_direction(x):
    if x == 1:
        return -1 
    return 1 

def search_roll_number(a,b):
    
    global have_to_roll

    d_index = [-1,1]
    

    for k in range(2): 
        new_a = a+d_index[k]

        if new_a in dic and k == 0:
            
            if (dic[a][6] != dic[new_a][2]) and not visited[new_a]:
    
                visited[new_a] = 1
                have_to_roll.append((new_a,next_direction(b)))
                search_roll_number(new_a,next_direction(b))

        elif new_a in dic and k == 1:
            
            if dic[a][2] != dic[new_a][6] and not visited[new_a]:

                visited[new_a] = 1
                have_to_roll.append((new_a,next_direction(b)))
                search_roll_number(new_a,next_direction(b))

    
        

def roll(dic, have_to_roll):

    
    while have_to_roll:
        
        num,direction = have_to_roll.pop()
        
        topni = dic[num]
        topni.rotate(direction)
        dic[num] = topni
        
    return dic
    
        
        
    
if __name__ == '__main__':

    dic = {}
    for i in range(4):
        dic[i+1] = deque(input())
    T = int(input())

    command = deque()
    for _ in range(T):
        a,b = map(int,input().split())
        command.append((a,b))

    
    while command:

        a,b = command.popleft()
        visited = [0] * (4+1)
        visited[a] = 1
        have_to_roll = [(a,b)]
    
        search_roll_number(a,b)

        dic = roll(dic,have_to_roll)
    
    answer = 0


    for i in range(4):
        if dic[i+1][0] == '1':
            answer += 2**i
    
    print(answer)
        

    

    


