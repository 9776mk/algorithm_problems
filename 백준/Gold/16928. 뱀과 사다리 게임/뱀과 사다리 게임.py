from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        n = queue.popleft()
        for i in range(1, 7):
            new = n + i
            if 0 < new <= 100 and not visited[new]:
                if new in dict_.keys():
                    new = dict_[new]

                if not visited[new]:
                    queue.append(new)
                    visited[new] = True
                    board_[new] = board_[n] + 1


N, M = map(int, input().split())
board_ = [0] * 101
visited = [False] * 101

dict_ = {}

for i in range(N + M):
    a, b = map(int, input().split())
    dict_[a] = b

bfs(1)
print(board_[100])