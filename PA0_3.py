def solution(n, arr1, arr2):
    answer = []
    arr = {}
    arrlist = []
    
    for i in range(n):
        arr[i] = bin(arr1[i] | arr2[i]).replace('0b', '')
        arrlist.append(str(arr.get(i)))
        
    for i in arrlist:
        if len(i) == n:
            answer.append((str(i).replace('1','#')).replace('0', ' '))
        else:
            answer.append(((str('0' * (n-len(i)) + i)).replace('1','#')).replace('0', ' '))
    
    return answer

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))