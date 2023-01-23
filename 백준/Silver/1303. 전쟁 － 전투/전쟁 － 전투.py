from collections import deque


def bfs(a, b, v):
    cnt = 1
    # 사방 탐색용 리스트 생성
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # dfs용 덱 생성
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < M
                and 0 <= ny < N
                and visited[nx][ny] == False
                and list_[nx][ny] == v
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt


N, M = map(int, input().split())
list_ = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


w_total, b_total = 0, 0


for i in range(N):
    for j in range(M):
        if list_[j][i] == "W" and visited[j][i] == False:
            w_total += bfs(j, i, "W") ** 2
        elif list_[j][i] == "B" and visited[j][i] == False:
            b_total += bfs(j, i, "B") ** 2

print(w_total, b_total)
