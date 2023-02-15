def solution(citations):
    citation = sorted(citations)
    answer = 0
    c = -1 
    
    while citation:
        answer = 0 
        c = citation.pop()
        
        for i in citations:
            if i>=c:
                answer += 1
        if answer>=c:
            return answer
    return 0

a = solution([3,0,6,1,5])
print(a)