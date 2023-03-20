T = int(input())

for test_case in range(1,T+1):
    word = input()
    rev_word = word[::-1]

    print(f'#{test_case} 1' if word == rev_word else f'#{test_case} 0')