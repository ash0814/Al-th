def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(1)
        else:
            try:
            	stack.pop()
            except:
                return False
    if len(stack) > 0:
        return False
    return True

print(solution(input()))
print(solution(input()))
print(solution(input()))
print(solution(input()))