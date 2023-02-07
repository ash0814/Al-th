def solution(brown, yellow):
    result = []
    w = int(brown / 2)
    h = 2
    while w:
        print(w * h)
        print(brown + yellow)
        if w * h == brown + yellow:
            result.append(w)
            result.append(h)
            break
        w -= 1
        h += 1
    print(result)
    return result


if __name__ == '__main__':
    brown = 10
    yellow = 2
    answer = [4, 3]

    if solution(brown, yellow) == answer:
        print("OK")
    else:
        print("KO")
