# 전체 학생 n명, 도난 학생 lost, 여벌 학생 reserve
# n - lost(-reserve)

def solution(n, lost, reserve):
    real_lost = []
    for lost_stu in lost:
        if lost_stu in reserve:
            reserve.remove(lost_stu)
        else:
            real_lost.append(lost_stu)
    real_lost.sort()
    reserve.sort()
    lost = real_lost
    real_lost = []
    for stu in lost:
        if stu - 1 in reserve:
            reserve.remove(stu - 1)
        elif stu + 1 in reserve:
            reserve.remove(stu + 1)
        else:
            real_lost.append(stu)
    answer = n - len(real_lost)
    return answer