import sys
from collections import deque
input = sys.stdin.readline

# dfs 정리
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# bfs 정리
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 값 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

# 인접 리스트 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# 인접 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
# dfs 실행 후 방문 리스트 다시 초기화
visited = [False] * (n + 1)
print()
bfs(v)