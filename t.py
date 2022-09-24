from email.policy import default


def solution(n, m, x, y, r, c, k):

    
    x-=1
    y-=1
    c-=1
    r-=1
    dic = {}
    dic['l'] = [0,-1]
    dic['r'] =[0,1]
    dic['u'] =[-1,0]
    dic['d'] =[1,0]
    dis = abs(x-r)+abs(y-c)
# d l r u 
    sub = []
    if (k-dis)%2 != 0:
        return "impossible"

    if dis>k:
        return 'impossible'

    
    if abs(x-r) != 0:
        if x>r:
           sub.append('u'*abs(x-r))
        elif x<r:
            sub.append('d'*abs(x-r))
    
    if abs(y-c) != 0:
        if y>c:
            sub.append('l'*abs(y-c))
        elif y<c:
            sub.append('r'*abs(y-c))
        

    string = ''
    for i in sorted(sub):
        string += i

    

    cnt_u = r
    cnt_d = n-r-1
    cnt_r = m-c-1
    cnt_l = c


    def search_ns(s):
        if s=='l':
            ns = 'r'
        elif s == 'r':
            ns = 'l'
        elif s == 'u':
            ns= 'd'
        else:
            ns = 'u'
        return ns

    leng = (k- len(string)) // 2


    if leng == 0 :
        return string 
    
    answer_dic = {}
    answer_dic['d'] = cnt_d
    answer_dic['u'] = cnt_u
    answer_dic['r'] = cnt_r
    answer_dic['l'] = cnt_l

    temp = []
    ntemp = []
    for i in ['d','l','r','u']:
        if leng==0:
            break
        if answer_dic[i]<=leng:
            leng -= answer_dic[i] 
            temp.append(i*answer_dic[i])
            ntemp.append(search_ns(i)*answer_dic[i])
        
        else:
            
            temp.append(i*leng)
            ntemp.append(search_ns(i)*leng)
            leng = 0
    for i in sorted(temp):
        string+=i
    for i in sorted(ntemp):
        string+=i
    return string

    

ans = solution(2,3,2,3,2,2,5)
# ans = solution(3,3,1,2,2,2,3)
print(ans)
# print(ans)



0 0 0 
0 E S 
