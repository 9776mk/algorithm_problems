def solution(s):
    N = len(s)
    list_ = []
    cnt, answer = 0, 0
    for i in range(N):
        # 비어 있을 때 첫 글자 구하기
        if len(list_) == 0:
            list_.append(s[i])
        # 비어 있지 않을 때
        else:
            # 글자가 같은 경우 더 함
            if s[i] == list_[0]:
                list_.append(s[i])
            # 글자가 다른 경우
            else:
                # 다른 경우 cnt를 더함
                cnt += 1
                # 글자 수를 각가 비교해서 같다면
                if cnt == len(list_):
                    # 분해한 문자열의 개수로 반환한 후 리스트 초기화
                    answer += 1
                    list_ = []
                    cnt = 0
        # 마지막 글자로 분해되는 경우
        if i == N - 1 and len(list_) != 0:
            answer += 1

    return answer