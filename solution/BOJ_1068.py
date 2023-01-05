def search_tree(x):

    global answer 
    
    if x == R:
        return 
    
    if len(dic[x]) == 0:
        answer+=1 
    
    else:
        temp = [i for i in dic[x] if i != R]
        if len(temp) == 0: 
            answer+=1
        else:
            for key in temp:
                search_tree(key)
        
        

if __name__ == '__main__':
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    N = int(input())
    
    rootnode = list(map(int,input().split()))

    R = int(input())
    

    dic =defaultdict(list)
    answer = 0
    for idx,i in enumerate(rootnode):
        if i >= 0 :
            dic[i].append(idx)
        else:
            start_node = idx    
    
    if len(dic[start_node]) == 1 and dic[start_node][0] == R:
        print(1)
    else:
        search_tree(start_node)

        print(answer)

        
