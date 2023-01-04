import sys

def dfs(v):
    # 내가만든 int형은 전역변수로 선언
    global cnt

    if visited_num[v] == 0:
        cnt += 1
        visited_num[v] = cnt

    for i in N_[v]:
        # 0만 False, 나머지는 True
        if not visited_num[i]:
            dfs(i)


N, M, R = map(int, input().split())

N_ = [[] for _ in range(N + 1)]
visited_num = [0] * (N + 1)


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# print(N_)
# print(visited)

for i in range(M):
    a, b = map(int, input().split())
    N_[a].append(b)
    N_[b].append(a)


# 정렬
for j in range(N + 1):
    N_[j].sort()


cnt = 0

dfs(R)
# print(visited_num[1:])
for k in visited_num[1:]:
    print(k)
