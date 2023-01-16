while True:
    list_ = list(map(int, input().split()))

    if list_[0] == 0 and list_[1] == 0 and list_[2] == 0:
        break
    else:
        list_.sort()
        if list_[0] ** 2 + list_[1] ** 2 == list_[2] ** 2:
            print("right")
        else:
            print("wrong")