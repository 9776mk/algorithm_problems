T = int(input())

for test_case in range(1, T + 1):
    S = input()
    cnt = S.count('x')
    len_ = len(S)
    
    if cnt < 8:
        print(f'#{test_case} YES')
        
    else:
        if len_ - cnt >= 7:
            print(f'#{test_case} YES')
        else:
            print(f'#{test_case} NO')