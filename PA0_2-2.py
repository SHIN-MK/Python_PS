def solution(X, Y):
    answer = ''
    num_XY = []
    
    for i in (set(X) & set(Y)):
        num_XY.extend([i] * min(X.count(i), Y.count(i)))
        
    num_XY.sort(reverse=True)
    
    if not num_XY:
        return '-1'
    
    if num_XY[0] == '0':
        return '0'
    
    answer = ''.join(num_XY)
    
    return answer

solution('12321', '42531')