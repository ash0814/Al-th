from functools import cmp_to_key


def compare(x, y):
    str_x = str(x)
    str_y = str(y)

    xy = str_x + str_y
    yx = str_y + str_x
    if xy > yx:
        return -1
    else:
        return 1


def solution(numbers):
    result = ''
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    print(sorted_numbers)
    for num in sorted_numbers:
        result += str(num)
    print(result)
    result = int(result)
    return str(result)


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    answer = "9534330"
    if solution(numbers) == answer:
        print("OK")
    else:
        print("KO")
