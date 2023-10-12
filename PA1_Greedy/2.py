def solution(name):
    answer = 0
    min_cursor = len(name) - 1
    name = {i:name[i] for i in range(len(name))}
       
    for i in range(len(name)):
        
        answer += min(ord(name[i]) - ord('A'), 26 - (ord(name[i]) - ord('A')))     
        
        tmp = i + 1
        while tmp < len(name) and name[tmp] == 'A':
            tmp += 1
            
        min_cursor = min(min_cursor, 2*i + len(name) - tmp, i + 2*(len(name)-tmp))
            
    return answer + min_cursor


solution("JEROEN")