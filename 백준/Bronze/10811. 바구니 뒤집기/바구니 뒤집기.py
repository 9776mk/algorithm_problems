N, M = map(int, input().split())

list_ = []

for i in range(1, N + 1):
    list_.append(i)

# print(list_)

for i in range(M):
    a, b = map(int, input().split())

    N = b - a

    if N == 0:
        continue

    elif N == 1:
        list_[a - 1], list_[b - 1] = list_[b - 1], list_[a - 1]

    else:
        if N % 2 == 0:
            for j in range(0, N//2):
                list_[a - 1 + j], list_[b - 1 - j] = list_[b - 1 - j], list_[a - 1 + j]
        else:
            for j in range(0, (N + 1)//2):
                list_[a - 1 + j], list_[b - 1 - j] = list_[b - 1 - j], list_[a - 1 + j]

for k in list_:
    print(k, end=" ")