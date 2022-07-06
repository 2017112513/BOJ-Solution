a,b,v = map(int,input().split())
answer = (v-b)/(a-b)
print(answer)
if int(answer)==answer:
    print(int(answer))
else:
    print(int(answer)+1)

