def solution(progresses, speeds):
    answer = []
    while (len(progresses) != 0 and progresses[0] < 100):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if (progresses[0] >= 100):
            cnt = 0
            while (len(progresses) != 0 and progresses[0] >= 100):
                cnt += 1
                del progresses[0]
                del speeds[0]
            answer.append(cnt)
    return answer

print(solution(list(map(int, input().split())), list(map(int, input().split()))))