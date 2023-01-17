def solution(board):
    N = len(board)

    list_ = [[0] * N for _ in range(N)]

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                list_[x][y] = 1

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < N and 0 <= ny < N and list_[nx][ny] == 0:
                        list_[nx][ny] = 1

    answer, danger = 0, 0

    for j in range(N):
        for k in range(N):
            if list_[j][k] == 1:
                danger += 1

    answer = N * N - danger
    return answer