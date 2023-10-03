def solution(X, Y):
    answer = ''
    
    num_X = [] # X의 자릿수 --> 123 --> [1,2,3] 542 --> [5, 4, 2]
    num_Y = []
    num_XY = []
    
    for i in str(X):
        num_X.append(i)
        
        print(num_X)
        
    for i in str(Y):
        num_Y.append(i)
        
        print(num_Y)
        
    for i in num_X:
        if i in num_Y:
            num_XY.append(i)
            num_Y.remove(i)
            print(num_XY)
            print(num_Y)
        else:
            pass      
                
    if not num_XY:
        return '-1'
    else:
        answer = ''.join(sorted(num_XY, reverse=True))
        
        if int(answer) == 0:
            return '0'
        else:
            return answer
        
print(solution(5525, 125))