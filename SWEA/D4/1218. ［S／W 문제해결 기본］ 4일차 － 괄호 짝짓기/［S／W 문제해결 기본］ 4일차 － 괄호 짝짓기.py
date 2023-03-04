
for test_case in range(1, 11):
    N = int(input())
    list_ = list(map(str, input()))

    # print(list_)

    is_paried = 1

    gh_1 = []
    gh_2 = []
    gh_3 = []
    gh_4 = []

    for gh in list_:
        if gh == '(':
            gh_1.append(gh)
        elif gh == ')':
            if len(gh_1) != 0:
                gh_1.pop()
            else:
                is_paried = 0
                break
        elif gh == '[':
            gh_2.append(gh)
        elif gh == ']':
            if len(gh_2) != 0:
                gh_2.pop()
            else:
                is_paried = 0
                break
        elif gh == '{':
            gh_3.append(gh)
        elif gh == '}':
            if len(gh_3) != 0:
                gh_3.pop()
            else:
                is_paried = 0
                break
        elif gh == '<':
            gh_4.append(gh)
        elif gh == '>':
            if len(gh_4) != 0:
                gh_4.pop()
            else:
                is_paried = 0
                break
                
    print(f'#{test_case}', end=' ')
    if is_paried == 1 and gh_1 == [] and gh_2 ==[] and gh_3 ==[] and gh_4 == []:
        print(1)
    else:
        print(0)