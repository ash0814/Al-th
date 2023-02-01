def solution(array, commands):
    result = []
    for l in commands:
        i = l[0]
        j = l[1]
        k = l[2]
        l_slice = array[i - 1:j]
        l_slice.sort()
        result.append(l_slice[k - 1])
    return result


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = [5, 6, 3]

    result = solution(array, commands)
    if result == answer:
        print("OK")
    else:
        print("KO")
