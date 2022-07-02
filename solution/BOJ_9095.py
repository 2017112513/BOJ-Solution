T = int(input())
def s(n):
  if n ==1:
    return 1
  if n==2:
    return 2
  if n==3:
    return 4
  if n>3 :
    return s(n-1)+s(n-2)+s(n-3)

for i in range(T):
  n =int(input())
  print(s(n))


