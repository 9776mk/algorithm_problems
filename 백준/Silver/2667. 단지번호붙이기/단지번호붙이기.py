from collections import deque

def dfs(a, b):
    queue = deque()
    queue.append((a, b))
    cnt = 1

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and visited[nx][ny] == False
                and graph[nx][ny] == 1
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt


# 사방 탐색용
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


total_ = 0
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and visited[i][j] == False:
            total_ += 1
            result.append(dfs(i, j))

print(total_)
result.sort()
for i in result:
    print(i)
