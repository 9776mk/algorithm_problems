T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    for i in range(1, 10):
        if N % i == 0:
            j = N // i
            if 0 < j < 10:
            	print(f'#{test_case} Yes')
            	break
    else:
        print(f'#{test_case} No')