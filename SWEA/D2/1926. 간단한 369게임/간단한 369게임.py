# 3, 6, 9가 들어갈 때마다 -를 출력
# 33, 36, 39 같이 여러개가 들어가면 그 갯수만큼 --를 출력해야함.
N = int(input()) #N을 입력받음

list_369 = ['3','6','9'] # 3,6,9 리스트를 만듦

for number in range(1, N+1): # 1~N 까지의 범위에서
    cnt = 0 # cnt = 0
    for j in str(number): # number라는 글자 안에
        if j in list_369: #3,6,9가 들어 있을 때마다
            cnt+= 1 # cnt에 1씩 더 해준다.
    if cnt > 0: # 만약 cnt가 0이 아니라면, 즉 3,6,9가 적어도 하나는 들어있으면
        number = '-' * cnt # number에 cnt 횟수만큼 '-'를 곱해준다.
    print(number, end=' ') #그리고 number를 출력한다.