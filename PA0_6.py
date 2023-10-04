from itertools import combinations

def solution(orders, course):
    answer = []
    num_orders = set()
    combs = []
    
    # 중복된 메뉴 찾기
    for i in orders:
        for j in i:
            num_orders.add(j)
            
            
    # 메뉴의 조합 찾기        
    for i in course:
        combs.extend(list(combinations(num_orders, i)))
    
    # 메뉴의 조합이 주문한 메뉴에 있는지 확인
    counts = {}
    for i in combs:
        count = 0
        for j in orders:
            if all(k in j for k in i):
                count += 1
        if count >= 2:
            counts[i] = count
            
    # course에 맞는 가장 많이 주문된 메뉴 조합 찾기
    for i in course:
        max_count = 0
        for j in counts:
            if len(j) == i and counts[j] > max_count:
                max_count = counts[j]
                
        for j in counts:
            if len(j) == i and counts[j] == max_count:
                answer.append(''.join(sorted(j)))
 
    answer.sort()
        
    return answer