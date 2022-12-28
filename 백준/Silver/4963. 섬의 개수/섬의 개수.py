from collections import deque

# 출력 함수 정의
def pprint(n):
    for i in n:
        print(i)

# bfs 정의
def bfs(a, b):
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if map_[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 팔방 탐색
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1,-1, 0, 0, 1, 1, 1]

queue = deque()

while True :
    cnt = 0
    w, h = map(int, input().split())
    map_ = []
    for i in range(h):
        map_.append(list(map(int, input().split())))
    # pprint(map_)

    visited = [[False] * w for _ in range(h)]

    if w == 0 and h == 0:
        break

    # i가 높이 즉 y좌표, j가 가로 x 좌표
    for i in range(h):
        for j in range(w):
            if map_[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                cnt += 1

    print(cnt)