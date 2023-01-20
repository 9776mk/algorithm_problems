from collections import deque


def solution(numbers, direction):
    answer = deque()

    for i in numbers:
        answer.append(i)

    if direction == "right":
        n = answer.pop()
        answer.appendleft(n)

    else:
        n = answer.popleft()
        answer.append(n)

    return list(answer)