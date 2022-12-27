def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    len_ = len(babbling)

    for i in range(len_):
        for word in words:
            if word in babbling[i]:
                babbling[i] = babbling[i].replace(word, " ")
                # print(babbling)
                # print(len(babbling))
                # ['  ', 'uuu ', ' ', '   ', ' a']


    # 공백들을 없애줌
    new_li = [i.replace(" ", "") for i in babbling]
    # ['', 'uuu', '', '', 'a']


    answer = 0
    for i in new_li:
        if i == "":
            answer += 1

    return answer