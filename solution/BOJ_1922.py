def main():
    def GetParent(x):
        if parent[x]==x:
            return x
        return GetParent(parent[x])

        
    def FindParent(a,b): # 같은 부모를 가지는지 확인하는 함수 
        a = GetParent(a)
        b = GetParent(b)
        if a==b:
            return 1
        return 0

    def Union(a,b): # 두 노드의 부모를 통합하는 함수 
        a = GetParent(a)
        b = GetParent(b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b



    import sys
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    parent = [0]*(N+1)

    for i in range(1,N+1):
        parent[i] = i

    distance = []


    for _ in range(M):
        a,b,c = map(int,input().split())
        distance.append((c,a,b))

    distance = sorted(distance ,key=lambda x: x[0])

    answer= 0
    total = 1
    for dis,node1,node2 in distance:
        if total == N:
            break
        if not FindParent(node1,node2):
            Union(node1,node2)
            answer+=dis
            total+=1
        else:
            continue
            
    print(answer)

main()

