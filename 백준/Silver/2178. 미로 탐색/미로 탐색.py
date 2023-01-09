import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    global cnt
    queue = deque()
    queue.append((a, b))
    route[a][b] = cnt

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < N and -1 < ny < M:
                # 길을 방문하지 않았다면
                if list_[nx][ny] == "1" and route[nx][ny] == 0:
                    route[nx][ny] = route[x][y] + 1
                    cnt += 1
                    queue.append((nx, ny))


N, M = map(int, input().split())

list_ = []
for _ in range(N):
    list_.append(list(input()))

for i in range(N):
    list_[i].pop()

route = [[0] * M for _ in range(N)]


cnt = 1

bfs(0, 0)
print(route[N - 1][M - 1])
