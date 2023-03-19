T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    pascal = [[] for _ in range(N)]
    
    if N == 1:
        pascal[0] = [1]
    
    elif N >= 2:
        pascal[0] = [1]
        pascal[1] = [1,1]

        # a[i][j] = a[i-1][j-1] + a[i-1][j]
        for i in range(2, N):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    pascal[i].append(1)
                else:
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])

    print(f'#{test_case}')
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=" ")
        print()