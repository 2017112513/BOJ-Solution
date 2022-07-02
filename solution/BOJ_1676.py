
import sys
input = sys.stdin.readline
def factorial(n):
    if n == 1:
        return 1
    if n>=2:
        return n*factorial(n-1)

num = str(factorial(int(input())))
print(len(num)-len(num.rstrip('0')))