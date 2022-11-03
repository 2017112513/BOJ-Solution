arr = [4,5]


def solution(arr):
    
    def f(array):

        if len(array)%2==0: # 배열의 길이가 짝수일경우
            
            n = len(array)//2

            temp_1 = array[:n]
            temp_1 = temp_1[::-1]

            temp_2 = array[n:]
            temp_2 = temp_2[::-1]

        else:
            n = len(array)//2

            temp_1 = array[:n+1]
            temp_1 = temp_1[::-1]

            temp_2 = array[n+1:]
            temp_2 = temp_2[::-1]

        return temp_1,temp_2

    if len(arr) == 1:
        return arr

    arr = arr[::-1] # 1단계 : 배열을 뒤집는 함수
    answer = []

    temp_1,temp_2 = f(arr)

    ans_1,ans_2 = f(temp_1)
    ans_3,ans_4 = f(temp_2)
    
    answer = ans_1+ans_2+ans_3+ans_4
    return answer

a= solution(arr)
print(a)