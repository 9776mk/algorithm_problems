from collections import deque

n, m = map(int, input().split())
graph = []


# [[0,0] x m] x n로 리스트를 생성한 후 앞쪽은 벽파괴 가능한 경우, 뒤쪽은 불가능한 경우로 나눔
# 즉, visited[x][y][0]은 벽 파괴 가능한 경우, [x][y][1]은 불가능한 경우 두 가지로 리스트를 생성.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        x, y, z = queue.popleft()
        # 끝에 도착하면 바로 출력하여 최솟값 만족
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 사방 탐색 결과가 범위를 벗어나지 않을 때,
            if -1 < nx < n and -1 < ny < m:
                # 다음 이동할 곳이 벽이고, 벽을 아직 부수지 않은 경우(벽을 부순 경우로 큐에 추가)
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                # 다음 이동할 곳이 길이고, 아직 한 번도 방문하지 않은 곳이면 (벽을 부수거나 부수지 않은 것은 상관x)
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1


print(bfs(0, 0, 0))