def solution(participant, completion):
    # # list로 풀기 1 : 효율성 테스트 fail : O(n^2)
    # for person in completion:
    #     if person in participant:
    #         participant.remove(person)
    # return participant[0]


	# # list로 풀기 2 : pass O(n)
    # participant.sort()
    # completion.sort()
    # for i in range(len(participant)):
    #     try:
    #         if participant[i] != completion[i]:
    #             answer = participant[i]
    #             break
    #     except:
    #         answer = participant[i]
    # return answer
    
    
    # # hash로 풀기 : 효율성 결과 best
    part = {}
    comp = {}
    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
    for j in completion:
        if j in comp:
            comp[j] += 1
        else:
            comp[j] = 1
    for key in part.keys():
        if not key in comp or part[key] != comp[key]:
            return key