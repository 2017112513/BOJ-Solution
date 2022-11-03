def main():
    
    def getParent(school,root,a):
        if root[a] == a:
            return a
        return getParent(school,root,root[a])
   

    def findParent(school,root,a,b): # 두 노드의 부모가 같은지 비교 

        a = getParent(school,root,a)
        b = getParent(school,root,b)
   
        if a==b:
            return 1
        return 0
 
    
    def unionParent(school,root,a,b):

        a = getParent(school,root,a)
        b = getParent(school,root,b)

        if a<b:
            root[b] = a
        else:
            root[a] = b

    import sys
    input = sys.stdin.readline
    from collections import deque

    N,M = map(int,input().split())

    school = deque(input().strip().split())
    school.appendleft('_')  # index 를 맞춰주기 위해 

    lis = []

    root = [0]*(N+1)

    for i in range(1,N+1):
        root[i] = i
    

    for _ in range(M):
        a,b,c = map(int,input().split())
        if school[a] == school[b]:
            continue
        lis.append((c,a,b))


    lis = sorted(lis,key=lambda x: x[0])

    answer = 0
    total = 1
    for i,l in enumerate(lis,start = 1):

        
        distance,node1,node2 = l[0],l[1],l[2]

        if total == N:
            break

        if not findParent(school,root,node1,node2):

            unionParent(school,root,node1,node2)
            answer+=distance
            total+=1

    if total == N:
        print(answer)
    else:
        print(-1)

main()