def main():
    import sys
    input = sys.stdin.readline

    

    def getParent(root,a):
        if root[a] == a:
            return a
        return getParent(root,root[a])
    
    def findParent(root,a,b):
        
        a = getParent(root,a)
        b = getParent(root,b)

        if a==b:
            return 1
        return 0
    
    def unionParent(root,a,b):

        a = getParent(root,a)
        b = getParent(root,b)

        if a<b:
            root[b] = a
        else:
            root[a] = b
    while 1: 

        N,M = map(int,input().split())

        if N==0 and M==0:
            break

        cost = 0
        root = [i for i in range(N)]
        
        lis = []
        for _ in range(M):
            a,b,c = map(int,input().split())

            lis.append((c,a,b))

            cost+=c
        
        lis = sorted(lis,key=lambda x: x[0])

        total = 1
        save_cost = 0

        for dis,n1,n2 in lis:

            if total==N:
                break
                
            if not findParent(root,n1,n2):

                unionParent(root,n1,n2)
                total+=1
                print(n1,n2,dis)
                save_cost += dis

        
        print(cost-save_cost)

main()
    
