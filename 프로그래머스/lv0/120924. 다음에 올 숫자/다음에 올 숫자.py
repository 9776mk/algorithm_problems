def solution(common):
    n = len(common)
    answer = 0

    if common[1] - common[0] == common[n - 1] - common[n - 2]:
        answer = common[n - 1] + common[1] - common[0]

    else:
        answer = int(common[n - 1] * (common[1] / common[0]))

    return answer