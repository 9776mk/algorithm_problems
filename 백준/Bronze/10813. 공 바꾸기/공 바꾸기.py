N, M = map(int, input().split())

list_ = []

for i in range(1, N+1):
    list_.append(i)

for _ in range(M):
    a, b = map(int, input().split())
    list_[a-1], list_[b-1] = list_[b-1], list_[a-1]
        
for i in list_:
    print(i, end=" ")