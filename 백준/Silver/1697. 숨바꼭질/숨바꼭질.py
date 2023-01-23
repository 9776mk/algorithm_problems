from collections import deque


def bfs(v):
    global cnt, range_, N, K

    queue = deque()
    queue.append(v)
    list_[N] = cnt

    while True:
        n = queue.popleft()

        if 0 <= (2 * n) < range_ and list_[2 * n] == -1:
            list_[2 * n] = list_[n] + 1
            if 2 * n != K:
                queue.append(2 * n)

        if 0 <= n + 1 < range_ and list_[n + 1] == -1:
            list_[n + 1] = list_[n] + 1
            if n + 1 != K:
                queue.append(n + 1)

        if 0 <= n - 1 < range_ and list_[n - 1] == -1:
            list_[n - 1] = list_[n] + 1
            if n - 1 != K:
                queue.append(n - 1)

        if list_[K] != -1:
            break


range_ = 100001
list_ = [-1] * range_
N, K = map(int, input().split())
cnt = 0

bfs(N)
print(list_[K])
