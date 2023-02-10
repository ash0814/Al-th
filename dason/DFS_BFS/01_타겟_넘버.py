def dfs(numbers, target, index, sum_number):
    global result
    if index == len(numbers) - 1 and sum_number == target:
        result += 1
    if index == len(numbers) - 1:
        return
    dfs(numbers, target, index + 1, sum_number + numbers[index])
    dfs(numbers, target, index + 1, sum_number - numbers[index])


def solution(numbers, target):
    global result
    result = 0
    index = -1
    sum_number = 0
    dfs(numbers, target, index, sum_number)
    return result


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = 5
    if solution(numbers, target) == answer:
        print("OK")
    else:
        print("KO")
