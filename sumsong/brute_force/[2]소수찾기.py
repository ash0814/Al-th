from itertools import permutations

def raw_number(number):
    if number == 0 or number == 1:
        return False
    for n in range(2, number//2 + 1):
        if number % n == 0:
            return False
    return True

def solution(numbers):
    num_list = list(numbers)
    new_list = []
    for i in range(len(num_list)):
        for j in permutations(num_list, i+1):
            new_list.append(int(''.join(j)))
    new_set = set(new_list)
    print(new_set)
    answer = 0
    for n in new_set:
        if raw_number(n) is True:
            answer += 1
    return answer