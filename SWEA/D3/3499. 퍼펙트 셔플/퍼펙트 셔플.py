# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, 1+T):
    # 카드 수 입력
    N = int(input())
    list_ = list(map(str, input().split()))
    suffled_ = []

    # 리스트를 반으로 나누기
    # N이 짝수이면
    if N % 2==0:
        # 기존 리스트를 반으로 나눈 후
        half_N = int(N/2)
        list_A = list_[0:half_N]
        list_B = list_[half_N:N]
        # 번갈아가면서 하나씩 추가
        for i in range(half_N):
            suffled_.append(list_A[i])
            suffled_.append(list_B[i])

    # N이 홀수이면
    else:
        # 기존 리스트를 반으로 나눈 후
        half_N = int(N/2)+1
        list_A = list_[0:half_N]
        list_B = list_[half_N:N]
    
        # 번갈아가면서 하나씩 추가
        for i in range(half_N-1):
            suffled_.append(list_A[i])
            suffled_.append(list_B[i])
        # 남는 
        suffled_.append(list_A[half_N-1])
 
    print(f'#{test_case}', end=' ')
    for i in suffled_:
        print(i, end=' ')
    print()