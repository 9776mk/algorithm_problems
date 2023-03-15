import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS 함수
def dfs(node, color):
    # 제일 처음 방문한 정점은 
    visited[node] = color

    # 기준 정점과 연결된 모든 정점에서
    for neighbor in graph_[node]:
        # 이웃한 정점과 같은 색깔인 경우 False 반환
        if visited[neighbor] == color:
            return False
        # 아직 방문하지 않은 정점인 경우 색깔을 반대로 설정하여 DFS 수행
        if visited[neighbor] == -1:
            if not dfs(neighbor, 1 - color):
                return False
    # 모든 정점을 방문한 경우 True 반환
    return True


K = int(input())
for i in range(K):
    answer = True
    V, E = map(int, input().split())

    visited = [-1] * (V + 1)
    graph_ = [[] for _ in range(V + 1)]
    # print(graph_)

    for _ in range(E):
        a, b = map(int, input().split())
        graph_[a].append(b)
        graph_[b].append(a)


    # 모든 정점을 순회하며 DFS를 수행하여 이분 그래프인지 판별
    for i in range(V):
        if visited[i] == -1:
            if not dfs(i, 0):
                answer = False

    if answer:
        print("YES")
    else:
        print("NO")
