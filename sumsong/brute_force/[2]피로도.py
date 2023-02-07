from itertools import permutations

def solution(k, dungeons):
    max_case = 0
    max_solution = len(dungeons)
    for order in permutations(dungeons, max_solution):
        hp = k
        case = 0
        for dungeon in order:
            if hp >= dungeon[0]:
                case += 1
                hp -= dungeon[1]
        if case == max_solution:
            return case
        if case > max_case:
            max_case = case
    return max_case