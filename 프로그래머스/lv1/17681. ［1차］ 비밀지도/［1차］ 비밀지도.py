def solution(n, arr1, arr2):
    temp1, temp2 = [], []

    for i in range(n):
        temp1.append(format(arr1[i], "b").zfill(n))
        temp2.append(format(arr2[i], "b").zfill(n))

    answer = []

    for j in range(n):
        str = ""
        for k in range(n):
            if temp1[j][k] == "0" and temp2[j][k] == "0":
                str += " "
            else:
                str += "#"
        answer.append(str)

    return answer