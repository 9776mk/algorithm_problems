T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())
    r  = N/10 #최대 학생 숫자
    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    rank = 0
    score = [list(map(int, input().split())) for _ in range(N)] 
    total_score = []
    k_score = 0

    
    for i in range(N):
        sum = 0
        for j in range(3):
            if (j==0):
                sum += 0.35 * score[i][j]
            elif(j==1):
                sum += 0.45 * score[i][j]
            else:
                sum += 0.2 * score[i][j]
        total_score.append(sum) #총점 리스트 생성
    k_score = total_score[K-1] #찾으려는 학생의 점수 저장
    total_score.sort(reverse=True) #내림차순으로 정리
    a = total_score.index(k_score)
    rank = int(a/r)
    grade = grade_list[rank]
    
    print('#%d %s' %(test_case, grade))