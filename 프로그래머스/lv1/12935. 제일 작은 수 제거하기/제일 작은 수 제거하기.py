def solution(arr):
    answer = []
    min_ = min(arr)
    
    for i in arr:
        if i == min_:
            continue
        else:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    
    return answer