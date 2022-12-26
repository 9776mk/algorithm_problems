N, k = map(int, input().split())

list_ = list(map(int, input().split()))
list_.sort(reverse=True)

print(list_[k - 1])