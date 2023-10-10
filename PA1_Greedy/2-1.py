def solution(name):
    answer = 0
    min_cursor = len(name) - 1
    
    for i, _name in enumerate(name):
        answer += min(ord(_name) - ord('A'), ord('Z') - ord(_name) + 1)
        
        tmp = i + 1
        while tmp < len(name) and name[tmp] == 'A':
            tmp += 1
            
        min_cursor = min(min_cursor, i + i + len(name) - tmp)
         
    return answer + min_cursor


solution("BBAAAABBB")