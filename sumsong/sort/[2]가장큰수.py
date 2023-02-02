def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    answer = ''.join(n for n in numbers)
    return str(int(answer))

print(solution(list(input().split())))
