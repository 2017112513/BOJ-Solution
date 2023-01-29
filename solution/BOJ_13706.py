import sys
import math
input = sys.stdin.readline

def binary_search(N):
    right = N
    left = 1


    while left<=right:
        mid = (left + right)  // 2
 
        temp = mid**2

        if temp == N:
            return mid
        
        if temp < N : 
            left = mid
        else:
            right = mid

if __name__ == '__main__':

    N = int(input())

    answer = binary_search(N)

    print(answer)