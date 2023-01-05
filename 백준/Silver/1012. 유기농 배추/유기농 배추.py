from collections import deque
import sys
input = sys.stdin.readline
from pprint import pprint

# 사방탐색용
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# bfs 정의
def bfs(graph, a, b):
    # deque으로 선언한뒤 제일 처음 좌표를 넣음
    queue = deque()
    queue.append((a,b))

    # visited대신 해당 그래프의 값을 0으로 만들어줌
    graph[a][b] = 0

    # queue가 비면 종료
    while queue:
        # queue에 저장된 값을 뺀 후
        x, y = queue.popleft()
        
        # 사방탐색 진행
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 사방탐색의 범위가 인덱스를 벗어나면
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                # 다음 진행
                continue
            # 값이 1이라면, 그 값을 0으로 만들고 queue에 집어넣기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

# 사용자 입력을 받음
t = int(input())
for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    # 그래프를 0으로 초기화 한 뒤
    graph = [[0] * m for _ in range(n)]

    # 입력 받은 값들을 1로 바꿔줌
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)