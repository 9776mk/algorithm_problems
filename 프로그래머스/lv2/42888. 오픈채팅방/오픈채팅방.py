def solution(record):
    dict_ = {}

    for rcd in record:
        if "Enter" in rcd or "Change" in rcd:
            msg, uid, nickname = rcd.split()
            dict_[uid] = nickname
            
    answer = []
    for rcd in record:
        if "Enter" in rcd:
            msg, uid, nickname = rcd.split()
            answer.append(f"{dict_[uid]}님이 들어왔습니다.")

        elif "Leave" in rcd:
            msg, uid = rcd.split()
            answer.append(f"{dict_[uid]}님이 나갔습니다.")

    return answer