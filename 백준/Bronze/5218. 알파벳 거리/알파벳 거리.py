N = int(input())

for i in range(N):
    w1, w2 = map(str, input().split())
    answer = []

    for i in range(len(w1)):
        A, B = int(ord(w1[i])) - 64, int(ord(w2[i])) - 64

        if B >= A:
            answer.append(B - A)
        else:
            answer.append(B + 26 - A)

    print("Distances: ", end="")
    for s in answer:
        print(s, end=" ")
    print("")