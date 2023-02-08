from itertools import product

def solution(numbers, target):
    answer = 0
    # 완전탐색으로 풀었음
    combi = []
    for n in numbers:
        combi.append([n, -n])
    for num in product(*combi):
        if sum(num) == target:
            answer += 1
    return answer