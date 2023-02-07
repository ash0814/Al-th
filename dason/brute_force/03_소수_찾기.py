from itertools import permutations


def checkSosu(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def solution(numbers):
    result = 0
    l: list = []
    sosu: list = []
    for num_len in range(1, len(numbers) + 1):
        permutations_list = list(permutations(numbers, num_len))
        string = ""
        for tup in permutations_list:
            string = ''.join(tup)
            num = int(string)
            if l.count(num) == 0 and num != 0 and num != 1:
                l.append(num)
                if checkSosu(num):
                    result += 1
    print(result)
    return result


if __name__ == '__main__':
    numbers = "011"
    answer = 3
    if solution(numbers) == answer:
        print("OK")
    else:
        print("KO")


