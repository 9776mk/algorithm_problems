# 연결 요소의 개수 = 연결되지 않은 것들
# BFS를 한 번 돌려서 연결된 것들은 True, 연결되지 않으면 False
# False인 원소중 하나를 골라 BFS를 돌려 연결되면 True, 연결되지 않으면 False 카운트 +1
# True가 없어질 떄까지 반복

# 정점 개수 n, 간선 개수 m 입력
n, m = map(int, input().split())

# 각 정점마다 간선을 입력할 간선 리스트 선언
# 1부터 시작하므로 정점 개수 +1
list_ = [[] for _ in range(n+1)]

# 방문을 기록할 리스트 선언
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    list_[a].append(b)
    list_[b].append(a)

def dfs(start):
    # 시작하는 노드를 스택에 넣고
    stack = [start]
    # 방문 처리
    visited[start] = True

    # 스택이 비어 있지 않은 동안
    while stack:
        # stack에서 꺼낸 값을 현재 값으로 설정
        cur = stack.pop()

        # list_[cur]에 있는 인접값들을 보고
        for adj in list_[cur]:
            # 인접값들을 방문하지 않았다면
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

cnt = 0

# visited[i]에서 False가 사라질 때까지
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
    else:
        continue

print(cnt)