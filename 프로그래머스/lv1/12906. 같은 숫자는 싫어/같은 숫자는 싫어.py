def solution(arr):
    temp = arr[0]
    answer = []
    answer.append(temp)

    for i in range(len(arr)):
        if arr[i] == temp:
            continue
        else:
            answer.append(arr[i])
            temp = arr[i]
    return answer