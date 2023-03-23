T = int(input())
num_ = {1,2,3,4,5,6,7,8,9}

for test_case in range(1, T+1):
    sudoku = []
    for _ in range(9):
        list_ = list(map(int, input().split()))
        sudoku.append(list_)
#    print(sudoku)

    is_ok = True
# num_ = {1,2,3,4,5,6,7,8,9}
# sudoku = [[7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7], [8, 4, 7, 9, 3, 6, 1, 5, 2], [1, 5, 3, 8, 4, 2, 9, 7, 6], [9, 6, 2, 7, 5, 1, 8, 4, 3], [4, 2, 1, 3, 9, 8, 7, 6, 5], [3, 9, 5, 6, 7, 4, 2, 1, 8], [6, 7, 8, 2, 1, 5, 4, 3, 9]]

    # 행 검증
    for i in range(9):
        if set(sudoku[i]) != num_:
            is_ok = False
            break

    # 열 검증
    for i in range(9):
        list_col = []
        for j in range(9):
            list_col.append(sudoku[j][i])

        if set(list_col) != num_:
            is_ok = False
            break

    # 3 x 3 검증
    for i in range(0,9,3):
        for j in range(0,9,3):
            list_9 = []
            for k in range(3):
                for l in range(3):
                    #print(sudoku[i+k][j+l])
                    list_9.append(sudoku[i+k][j+l])
            if set(list_9) != num_:
                is_ok = False
                break

    if is_ok:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')