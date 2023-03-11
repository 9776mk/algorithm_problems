T = 10

for tc in range(1, T+1):
    a, b = map(str, input().split())

    stack_ = []

    for i in b:
        
        if stack_:
            if int(stack_[-1]) == int(i):
                stack_.pop()
            else:
                stack_.append(i)
        else:
            stack_.append(i)
    
    print(f'#{tc}', end=" ")
    for i in stack_:
        print(int(i), end="")
    print()