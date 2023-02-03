def solution(array, commands):
    answer = []
    temp = []
    for i in commands:
        print(i)
        temp = (array[i[0]-1:i[1]])
        print(temp)
        temp.sort()
        print(temp)
        answer.append(temp[i[2]-1])
    return answer