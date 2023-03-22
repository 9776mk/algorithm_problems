T = int(input())

for test_case in range(1, T+1):

    # 사용자로부터 입력을 받고
    N, K = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(N)]

    # list_의 값을 확인해서 1이면 가로(세로) list에 값을 저장하고, 0이면 이때까지의 list를 확인하여 list의 길이가 K인 경우 카운트를 하는 방법을 사용
    # list_의 맨마지막에 1인 경우는 연산이 일어나지 않으므로 따로 조건을 생성

    # 가로의 갯수를 먼저 계산
    garo_ = 0
    for i in range(N):
        garo_list = []
        for j in range(N):
            # 끝에 도달했는데 흰색 부분인 경우
            # 끝에 도달했다는 조건이 먼저 있어야 중복되지 않음
            if j == N-1 and list_[i][j] == 1:
                # 문자를 추가하고
                garo_list.append(1)
                # 리스트의 길이가 K인지 확인해서 K이면 카운트
                if len(garo_list) == K:
                    garo_ += 1

            # 흰색 부분인 경우 문자 추가
            elif list_[i][j] == 1:
                garo_list.append(1)

            # 검은색 부분인 경우
            elif list_[i][j] == 0:
                # 이때까지의 길이가 K이면 추가
                if len(garo_list) == K:
                    garo_ += 1

                garo_list.clear()

    # 세로의 경우 계산
    # 열을 계산하기 위해 list_[i][j]에서 list_[j][i]로 바꿔줌
    sero_ = 0
    for i in range(N):
        sero_list = []
        for j in range(N):
            # 끝에 도달했는데 흰색 부분인 경우
            if j == N-1 and list_[j][i] == 1:
                # 문자를 추가하고
                sero_list.append(1)
                if len(sero_list) == K:
                    sero_ += 1

            # 흰색 부분인 경우 문자 추가
            elif list_[j][i] == 1:
                sero_list.append(1)

            # 검은색 부분인 경우
            elif list_[j][i] == 0:
                # 이때까지의 길이가 K이면 추가
                if len(sero_list) == K:
                    sero_ += 1

                sero_list.clear()
    
    # 가로와 세로의 값을 합해 총 갯수 출력
    print(f'#{test_case} {garo_ + sero_}')
