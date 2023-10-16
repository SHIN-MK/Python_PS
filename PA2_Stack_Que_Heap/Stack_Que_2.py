def solution(s):
    answer = True
    so = []
    
    for i in s:
        if i in '(':
            so.append(i)
        else:
            if so:
                so.pop()
            else:    
                answer = False
                  
    if so:
        answer = False
        
    return answer

solution("(()(")