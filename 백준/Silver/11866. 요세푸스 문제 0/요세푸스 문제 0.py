N, K = map(int, input().split())
# N, K = 7, 3

list_ = []
answer = []


for n in range(1, N + 1):
    list_.append(n)

#print(list_)

i = K - 1

while list_:
    len_ = len(list_)
    # 인덱스가 리스트의 현재 길이를 넘지 않을 때
    if i <= len_ - 1:
        answer.append(list_.pop(i))
        i += K - 1
    # 인덱스가 리스트의 현재 길이를 넘을 때
    else:
        answer.append(list_.pop((i % len_)))
        i = (i % len_) + (K-1)

print("<", end="")
for j in range(N):
    if j == N - 1:
        print(answer[j], end="")
        break
    print(answer[j], end=", ")
print(">")