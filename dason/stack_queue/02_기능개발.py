def solution(progresses, speeds):
    result = []
    while progresses:
        count = 0
        for index in range(len(progresses)):
            progresses[index] += speeds[index]
        if progresses[0] >= 100:
            for index in range(len(progresses)):
                if progresses[index] >= 100:
                    count += 1
                else:
                    break
            result.append(count)
            del progresses[:count]
            del speeds[:count]
    return result


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    answer = [2, 1]
    if solution(progresses, speeds) == answer:
        print("OK")
    else:
        print("KO")