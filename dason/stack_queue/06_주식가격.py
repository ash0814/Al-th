from collections import deque


def solution(prices):
    result = []
    for index in range(len(prices)):
        d = deque(prices[index + 1:])
        count = 0
        start = prices[index]
        while d:
            print(d[0], start)
            count += 1
            if d[0] < start:
                break
            d.popleft()
        result.append(count)
    print(result)
    return result


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    answer = [4, 3, 1, 1, 0]
    if solution(prices) == answer:
        print("OK")
    else:
        print("KO")
