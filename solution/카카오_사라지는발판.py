cap = 4 
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]



def solution(cap, n, deliveries, pickups):
    

    answer = -1

    deliveries_dic = {}
    pickups_dic = {}
    
    for idx,node in enumerate(deliveries,start = 1):
        deliveries_dic[idx] = node
    
    for idx,node in enumerate(pickups,start = 1):
        pickups_dic[idx] = node        

    
    


    return answer
