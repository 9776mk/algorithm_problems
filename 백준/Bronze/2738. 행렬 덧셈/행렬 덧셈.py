N, M = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(N):
    matrix_1.append(list(map(int, input().split())))

for j in range(N):
    matrix_2.append(list(map(int, input().split())))

# print(matrix_1)
# print(matrix_2)

for i in range(N):
    for j in range(M):
        print(matrix_1[i][j] + matrix_2[i][j], end=" ")
    print()