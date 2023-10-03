def solution(X, Y):
    answer = ''
    
    num_X = {}
    num_Y = {}
    num_XY = []
    
    for i in range(9, -1, -1):
        num_X[str(i)] = 0
        num_Y[str(i)] = 0
        
    for i in X:
        num_X[i] += 1
        
    for i in Y:
        num_Y[i] += 1
        
    for num, countX in num_X.items():
        countY = num_Y.get(num, 0)
        count = min(countX, countY)
        num_XY.extend([num] * count)
                
    if not num_XY:
        return '-1'
    
    answer = ''.join(num_XY)
    
    if '-' in answer:
        answer = '-' + answer[:-1]
        
    if int(answer) == 0:
        return '0'
    
    return answer
        
print(solution('5525532345', '51252553450555'))