from collections import deque

# 나이트의 위치 이동
dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]


def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))

    board_[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < L and -1 < ny < L and board_[nx][ny] == -1:
                board_[nx][ny] = board_[x][y] + 1
                queue.append((nx, ny))

        if board_[c][d] != -1:
            break


T = int(input())

for i in range(T):
    L = int(input())

    board_ = [[-1] * L for i in range(L)]
    # print(board_)

    n1, n2 = map(int, input().split())
    d1, d2 = map(int, input().split())

    bfs(n1, n2, d1, d2)
    print(board_[d1][d2])
