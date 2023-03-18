T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(N)]
    
    max_list = 0

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            sum_list = 0
            for a in range(0,M):
                for b in range(0,M):
                    #print(n_list[a+i][b+j])
                    sum_list += n_list[i+a][j+b]

            if (sum_list >= max_list):
                max_list = sum_list
            else:
                continue
    print('#%d %d' %(test_case, max_list))           