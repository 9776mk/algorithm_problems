N = 9

list_ = []

for i in range(N):
    list_.append(list(map(int, input().split())))

max_ = -1
row, col = 0, 0

for i in range(N):
    for j in range(N):
        if list_[i][j] > max_:
            max_ = list_[i][j]
            row = i + 1
            col = j + 1

print(max_)
print(row, col)