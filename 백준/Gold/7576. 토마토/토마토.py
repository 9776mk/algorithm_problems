from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and box_[nx][ny] == 0:
                queue.append((nx, ny))
                box_[nx][ny] = box_[x][y] + 1


M, N = map(int, input().split())
box_ = []


for i in range(N):
    box_.append(list(map(int, input().split())))

queue = deque()

for k in range(N):
    for j in range(M):
        if box_[k][j] == 1:
            queue.append((k, j))

bfs()
answer = 0

for k in range(N):
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