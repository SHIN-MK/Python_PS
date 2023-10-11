def solution(n, costs):
    #MST
    answer = 0
    bridge = 0
    p = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    
    def parent(i):
        if i != p[i]:
            p[i] = parent(p[i])
        return p[i]
    
    while bridge != n-1:
        i, j, k = costs.pop(0)
        
        if parent(i) != parent(j):
            root1 = parent(i)
            root2 = parent(j)
            p[root2] = root1
            
            answer += k
            bridge += 1
    
    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])