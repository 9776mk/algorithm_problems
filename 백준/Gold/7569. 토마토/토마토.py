from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()
        A = x // N

        # 상하좌우 인접한 토마토 큐에 넣기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            B = nx // N

            if (A == B) and 0 <= nx < N * H and 0 <= ny < M and box_[nx][ny] == 0:
                queue.append((nx, ny))
                box_[nx][ny] = box_[x][y] + 1

        # 높이가 인접한 토마토 큐에 넣기
        ux = x + N
        if ux < N * H and box_[ux][y] == 0:
            queue.append((ux, y))
            box_[ux][y] = box_[x][y] + 1

        lx = x - N
        if lx >= 0 and box_[lx][y] == 0:
            queue.append((lx, y))
            box_[lx][y] = box_[x][y] + 1


M, N, H = map(int, input().split())
box_ = []
for i in range(N * H):
    box_.append(list(map(int, input().split())))

queue = deque()

for n in range(N * H):
    for m in range(M):
        if box_[n][m] == 1:
            queue.append((n, m))

bfs()
answer = 0

for k in range(N * H):
    for j in range(M):
        if box_[k][j] == 0:
            answer = -1
            break
        else:
            if box_[k][j] > answer:
                answer = box_[k][j]

    if answer == -1:
        answer = 0
        break

print(answer - 1)