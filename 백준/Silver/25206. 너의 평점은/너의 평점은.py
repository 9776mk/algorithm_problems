N = 20
sum_ = 0
grade_ = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0,
}
cnt_ = 0


for i in range(N):
    A, B, C = map(str, input().split())
    if C == "P":
        continue
    else:
        for key in grade_.keys():
            if key == C:
                sum_ += grade_[key] * (float(B))
                cnt_ += float(B)

if cnt_ != 0:
    print(sum_ / cnt_)
else:
    print(0)