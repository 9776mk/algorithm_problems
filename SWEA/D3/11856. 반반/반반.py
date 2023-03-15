T = int(input())
for test_case in range(1, T + 1):
    S = input()
    if len(set(S)) == 2:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')