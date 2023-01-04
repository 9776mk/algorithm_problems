import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    # print(cnt)
    visited[v] = cnt

    while queue:
        now_node = queue.popleft()

        for i in N_[now_node]:
            if visited[i] == 0:
                cnt += 1
                # print(cnt)
                visited[i] = cnt
                queue.append(i)


N, M, R = map(int, input().split())
N_ = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

cnt = 1

for i in range(M):
    a, b = map(int, input().split())
    N_[a].append(b)
    N_[b].append(a)

for j in range(N + 1):
    N_[j].sort(reverse=True)

bfs(R)

for i in visited[1:]:
    print(i)
