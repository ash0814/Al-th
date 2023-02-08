from itertools import permutations


def solution(k, dungeons):
    max_result = 0
    d_count = len(dungeons)
    d_per = list(permutations(dungeons, d_count))
    for d_tuple in d_per:
        pirodo = k
        result = 0
        for d in d_tuple:
            if pirodo >= d[0]:
                pirodo -= d[1]
                result += 1
            else:
                break
        max_result = max_result if max_result > result else result
    return max_result


if __name__ == '__main__':
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    answer = 3
    if solution(k, dungeons) == answer:
        print("OK")
    else:
        print("KO")
