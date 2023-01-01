import sys
input = sys.stdin.readline

A,B = input().split()

answer = 999

for i in range(len(B) - len(A) + 1):
    temp = 0 
    for j in range(len(A)):
        if A[j] != B[i+j]:
            temp+=1
    answer = min(temp,answer)

print(answer)
        