# 모음 리스트 생성
vowel = ['a', 'e', 'i', 'o', 'u']

# 테스트 케이스 입력 받음
T = int(input())

for test_case in range(1, T+1):
    # 단어 입력 받음
    word_ = input()
    # 출력할 문자열 생성
    no_vowel = ''

    # 입력 받은 단어들을 한 글자씩 뽑아서
    for elem in word_:
        # 그 단어가 vowel 리스트 안에 없으면
        if elem not in vowel:
            # 새로운 문자열에 추가
            no_vowel += elem
        else:
            continue

    print(f'#{test_case} {no_vowel}')