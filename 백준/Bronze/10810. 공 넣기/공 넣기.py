N, M = map(int, input().split())

list_ = [0] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        list_[i] = c
        
for i in list_:
    print(i, end=" ")