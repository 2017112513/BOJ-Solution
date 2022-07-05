cnt=0
def solution(n,r,c):
  global cnt
  if n==0:
    return '마지막칸'
  if r<2**(n-1):
    if c<2**(n-1):
      return solution(n-1,r,c)
    elif c>=2**(n-1):
      
      c= c-2**(n-1)
      
      cnt+=(2**(n-1))*(2**(n-1))
      return solution(n-1,r,c)
  elif r>=2**(n-1):
    
    if c<2**(n-1):
        r= r-2**(n-1)
      
        cnt+=(2**(n-1))*(2**(n-1))*2
        return solution(n-1,r,c)
    elif c>=2**(n-1):
        r= r-2**(n-1)
        c= c-2**(n-1)
      
        cnt+=(2**(n-1))*(2**(n-1))*3
        return solution(n-1,r,c)
n,r,c=map(int,input().split())
solution(n,r,c)
print(cnt)