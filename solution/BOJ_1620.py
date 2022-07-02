import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic={}
num_dic = {} 
for i in range(1,n+1):
    name = input().strip()
    dic[name] = str(i)
    num_dic[str(i)]= name

for i in range(m):
    do = input().strip()
    if do in dic:
        print(dic[do])
    else:
        print(num_dic[do])