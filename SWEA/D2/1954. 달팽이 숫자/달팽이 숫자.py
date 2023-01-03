T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    snail_ =  [[0 for col in range(N)] for row in range(N)]

    #print(snail_)

    a = 0
    b = 0
    number_ = 1
    
    while number_ <= N*N:

        # 가로 [0][0] ~ [0][n-1] 1 ~ n (n번)
        for i in range(N-b):
            if number_ > N * N:
                break 
            snail_[a][a+i] = number_
            number_ += 1


        # 세로 [1][n] ~ [n-1][n-1] n ~ 2n-1 까지 (n-1번)
        for j in range(1, N-b):
            if number_ > N * N:
                break
            snail_[j+a][N-1-a] = number_
            number_ += 1

        # 가로 [n-1][n-2] ~ [n-1][0] 2n ~ 3n -2 까지 (n-1번) #거꾸로
        for k in range(2, N+1-b): 
            if number_ > N * N:
                break
            snail_[N-1-a][N-k-a] = number_
            number_ += 1

        # 세로 [n-2][0] ~ [n+2][0] 3n-1 부터 4n-3까지 (n-2번) #거꾸로
        for l in range(2,N-b):
            if number_ > N * N:
                break  
            snail_[N-a-l][a] = number_
            number_ += 1

        a += 1
        b += 2
        
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(snail_[i][j], end= ' ')
        print()    