T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    
    # 이득
    profit = 0
    # 최대 가격
    max_price = 0
    # 최소 인덱스, 최대 인덱스
    min_index, max_index = 0, 0

    while True:
        # 0부터 시작해서, 끝까지 돌아봤을 때
        for i in range(min_index, N):
            # 만약 현재 저장된 최대 가격보다 더 큰 가격이 있으면
            if max_price < price[i]:
                # 그 값을 최대가격으로 설정하고
                max_price = price[i]
                # 최대 가격일 때의 인덱스르 저장
                max_index = i

        # 현재 저장된 최소 인덱스에서 최대 인덱스까지
        for j in range(min_index, max_index):
            # 최대 가격 - 해당하는 각 가격의 합이 이득으로 저장
            profit += (max_price - price[j])
        
        # 이득을 보고 나면 최대 가격 초기화
        max_price = 0
        # 최소 index를 실행한 곳 다음으로 이동
        min_index = max_index+1

        # N까지 전부 진행이 되면
        if min_index == N:
            # 출력 후
            print(f'#{test_case} {profit}')
            # while문 종료
            break