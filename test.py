def search_next_curser(name,start_string,curr_curser,long,visited):

    diff = []
    for i in range(len(name)):

        if name[i] !=  start_string[i] and not visited[i]:
            
            diff.append(i)
    if len(diff)== 0:

        return -1
    
           
    m = 999

    for i in diff:
        temp = min(abs(long-i),abs(i-curr_curser)) 
        if temp<m:
            m = temp
            next_curser = i
        

    
    return next_curser

def calculate(start_string,name,next_curser,curr_curser,long,answer):
        # print(curr_curser,next_curser,'ncnc')
        step = min(abs(long-(next_curser-curr_curser)),abs(next_curser-curr_curser))
        next_string = name[next_curser]
        curr_string = start_string[curr_curser]
        curr_string_number = dic[curr_string]
        next_string_number = dic[next_string]
        # print(curr_string,next_string, next_string_number,curr_string_number,'zz')
        next_up_down = min(abs(next_string_number-curr_string_number),abs(26-abs(next_string_number-curr_string_number)))

        
        answer += next_up_down
        answer += step 
        print(step,next_up_down)
        return start_string,answer
    
alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {}
for idx, ab in enumerate(alphabet):
    dic[ab] = idx
    


def solution(name):
    

    answer = 0
    curr_curser  = 0
    long = len(name)
    start_string = 'A'*long
    
    visited = [0]*long
    
    while 1:
        next_curser = search_next_curser(name,start_string,curr_curser,long,visited)
        if next_curser == -1:
            break
        
        start_string,answer = calculate(start_string,name,next_curser,curr_curser,long,answer)
        curr_curser = next_curser   
        # print(curr_curser,'cc')
        visited[next_curser] = 1 
    return answer

a = solution('BBBBAAAABA')
