def solution(answers):
    answer = []
    sc1, sc2, sc3 = 0, 0, 0
    type1 = [1, 2, 3, 4, 5]
    type2 = [2, 1, 2, 3, 2, 4, 2, 5]
    type3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == type1[i % len(type1)]: sc1 += 1
        if answers[i] == type2[i % len(type2)]: sc2 += 1
        if answers[i] == type3[i % len(type3)]: sc3 += 1
    
    result = [sc1, sc2, sc3]
    for index, score in enumerate(result):
        if score == max(result): answer.append(index + 1)

    return answer