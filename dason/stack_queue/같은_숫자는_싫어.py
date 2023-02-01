def solution(arr):
    result = []
    for n in arr:
        if len(result) == 0:
            result.append(n)
        if result[-1] != n:
            result.append(n)
    return result


if __name__ == '__main__':
    arr = [1, 1, 3, 3, 0, 1, 1]
    answer = [1, 3, 0, 1]
    if solution(arr) == answer:
        print("OK")
    else:
        print("KO")
