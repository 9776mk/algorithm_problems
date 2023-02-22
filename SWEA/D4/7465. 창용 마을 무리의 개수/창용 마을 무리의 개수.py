# import sys

# sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for test_case in range(1, T+1):
    # N, M을 입력받음
    N, M = map(int, input().split())
    
    cnt = 0

    # 인접 리스트 생성용 빈 리스트
    graph_ = [[] for _ in range(N+1)]
    #print(graph_)

    # 인접 리스트 생성
    for _ in range(M):
        a, b = map(int, input().split())
        graph_[a].append(b)
        graph_[b].append(a)

    # print(graph_)

    # 방문 확인용 빈 리스트
    visited = [False] * (N + 1)

    #print(visited)

    def dfs(start):
        stack = [start]
        visited[start] = True

        while stack:
            cur = stack.pop()

            for adj in graph_[cur]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = True
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
        else:
            continue

    print(f'#{test_case} {cnt}')