# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    total_ = []

    for i in range(1,a+1):
        total_.append(i)

    handin_ = list(map(int, input().split()))

    total_ = set(total_)
    handin_ = set(handin_)

    no_handin_ = total_ - handin_
#    print(no_handin_)
    
    print(f'#{test_case}', end= ' ')
    for elem in no_handin_:
        print(elem, end=' ')
    print()